"""
Predictions Page: Shows Dixon-Coles match predictions for upcoming matches.
Auto-loads matches from the parser and displays predictions in a clean format.
"""

from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st
from scipy.stats import poisson
from scipy.optimize import minimize

from src.accent_utils import get_accent_insensitive_selectbox
from src.upcoming_matches_parser import get_upcoming_matches_from_file, format_match_date

# Verify authentication (set in Home.py)
if not st.session_state.get("authenticated", False):
    st.error("⚠️ Por favor, inicia sesión desde la [página principal](?)")
    st.stop()

st.set_page_config(page_title="Predicciones de Partidos", layout="wide")

# Styling
st.markdown("""
    <style>
    .prediction-row {
        display: flex;
        gap: 1rem;
        padding: 1.2rem;
        border-radius: 10px;
        background: linear-gradient(90deg, #f8fafc 0%, #f0f9ff 100%);
        border: 1px solid #bfdbfe;
        margin-bottom: 0.8rem;
        align-items: center;
    }
    .match-info {
        flex: 1;
        min-width: 250px;
    }
    .match-teams {
        font-weight: 700;
        font-size: 1.05rem;
        margin-bottom: 0.3rem;
    }
    .match-meta {
        font-size: 0.85rem;
        color: #666;
    }
    .prediction-odds {
        display: flex;
        gap: 0.5rem;
        flex-wrap: wrap;
        justify-content: flex-end;
        min-width: 400px;
    }
    .odd-box {
        padding: 0.6rem 0.9rem;
        border-radius: 8px;
        text-align: center;
        font-size: 0.9rem;
        font-weight: 600;
        border: 2px solid;
        min-width: 90px;
    }
    .odd-box-home {
        background: #dbeafe;
        border-color: #0284c7;
        color: #0c4a6e;
    }
    .odd-box-draw {
        background: #f3e8ff;
        border-color: #a855f7;
        color: #6b21a8;
    }
    .odd-box-away {
        background: #dcfce7;
        border-color: #22c55e;
        color: #15803d;
    }
    .odd-prob {
        font-size: 0.75rem;
        font-weight: 400;
        opacity: 0.9;
    }
    </style>
""", unsafe_allow_html=True)

# ============================================================================
# HEADER
# ============================================================================

st.markdown("""
    <div style="padding: 1.5rem 2rem; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); 
                border-radius: 16px; color: white; margin-bottom: 2rem;">
        <h1 style="margin: 0; font-size: 2rem;">⚡ Predicciones de Partidos</h1>
        <p style="margin: 0.5rem 0 0 0; opacity: 0.9; font-size: 1.05rem;">
            Modelo Poisson con home advantage por liga y time decay
        </p>
    </div>
""", unsafe_allow_html=True)

# ============================================================================
# LOAD MODEL DATA
# ============================================================================

PROJECT_ROOT = Path(__file__).parent.parent
DATA_PATH = PROJECT_ROOT / "event_data" / "processed" / "top5_events_current.parquet"

@st.cache_data
def load_model_data():
    """Load historical match data for model fitting"""
    try:
        df = pd.read_parquet(DATA_PATH)
        
        matches_data = []
        for match_id in df['matchId'].unique():
            match_events = df[df['matchId'] == match_id]
            teams = match_events['team_name'].unique()
            
            if len(teams) >= 2:
                team1, team2 = sorted(teams)[:2]
                first_row = match_events.iloc[0]
                
                team1_events = match_events[match_events['team_name'] == team1]
                team2_events = match_events[match_events['team_name'] == team2]
                
                goals1 = ((team1_events['Event Type'] == 'Goal') | (team1_events['LeadingToGoal'] == True)).sum()
                goals2 = ((team2_events['Event Type'] == 'Goal') | (team2_events['LeadingToGoal'] == True)).sum()
                
                matches_data.append({
                    'team1_name': team1,
                    'team2_name': team2,
                    'goals1': int(goals1),
                    'goals2': int(goals2),
                    'league': first_row['league'],
                    'match_date': pd.to_datetime(first_row['match_date']),
                })
        
        return pd.DataFrame(matches_data)
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return pd.DataFrame()


@st.cache_data
def fit_prediction_model(matches_df):
    """Fit the per-league home advantage model"""
    teams = sorted(list(set(matches_df['team1_name']) | set(matches_df['team2_name'])))
    leagues = sorted(list(matches_df['league'].unique()))
    
    team_idx = {team: i for i, team in enumerate(teams)}
    league_idx = {league: i for i, league in enumerate(leagues)}
    
    team1_idx = np.array([team_idx[t] for t in matches_df['team1_name']], dtype=int)
    team2_idx = np.array([team_idx[t] for t in matches_df['team2_name']], dtype=int)
    league_idx_arr = np.array([league_idx[l] for l in matches_df['league']], dtype=int)
    goals1 = matches_df['goals1'].values.astype(int)
    goals2 = matches_df['goals2'].values.astype(int)
    
    # Time decay weights
    max_date = matches_df['match_date'].max()
    days_ago = (max_date - matches_df['match_date']).dt.days.values
    weights = 2.0 ** (-days_ago / 90)
    
    n_teams = len(teams)
    n_leagues = len(leagues)
    
    params = np.concatenate([
        [np.log(1.0)],
        np.random.normal(0, 0.01, n_leagues),
        np.zeros(n_teams),
        np.zeros(n_teams),
    ])
    
    def neg_ll(x):
        mu = x[0]
        home_adv_league = x[1:1+n_leagues]
        attack = x[1+n_leagues:1+n_leagues+n_teams]
        defense = x[1+n_leagues+n_teams:]
        
        home_adv = home_adv_league[league_idx_arr]
        lambda1 = np.exp(mu + home_adv + attack[team1_idx] + defense[team2_idx])
        lambda2 = np.exp(mu + attack[team2_idx] + defense[team1_idx])
        
        ll = poisson.logpmf(goals1, lambda1) + poisson.logpmf(goals2, lambda2)
        return -np.sum(weights * ll)
    
    result = minimize(neg_ll, params, method='L-BFGS-B', options={'maxiter': 200})
    
    mu = result.x[0]
    home_adv_dict = {leagues[i]: result.x[1+i] for i in range(n_leagues)}
    attack_dict = {teams[i]: result.x[1+n_leagues+i] for i in range(n_teams)}
    defense_dict = {teams[i]: result.x[1+n_leagues+n_teams+i] for i in range(n_teams)}
    
    return mu, home_adv_dict, attack_dict, defense_dict, teams, leagues


def predict_match(team1, team2, league, mu, home_adv_dict, attack_dict, defense_dict):
    """Calculate match prediction"""
    ha = home_adv_dict.get(league, 0.0)
    lambda1 = np.exp(mu + ha + attack_dict.get(team1, 0) + defense_dict.get(team2, 0))
    lambda2 = np.exp(mu + attack_dict.get(team2, 0) + defense_dict.get(team1, 0))
    
    # Probabilities
    goal_range = np.arange(0, 10)
    p1 = poisson.pmf(goal_range, lambda1)
    p2 = poisson.pmf(goal_range, lambda2)
    
    home_win = np.sum([p1[i] * np.sum(p2[:i]) for i in range(1, len(goal_range))])
    draw = np.sum([p1[i] * p2[i] for i in range(len(goal_range))])
    away_win = np.sum([p1[i] * np.sum(p2[i+1:]) for i in range(len(goal_range)-1)])
    
    total = home_win + draw + away_win
    if total > 0:
        home_win /= total
        draw /= total
        away_win /= total
    
    return {
        'home_prob': home_win * 100,
        'draw_prob': draw * 100,
        'away_prob': away_win * 100,
        'home_odds': 1 / home_win if home_win > 0 else 999,
        'draw_odds': 1 / draw if draw > 0 else 999,
        'away_odds': 1 / away_win if away_win > 0 else 999,
        'xg_home': lambda1,
        'xg_away': lambda2,
    }


# ============================================================================
# MAIN INTERFACE
# ============================================================================

# Load model data
with st.spinner("📊 Cargando y ajustando modelo..."):
    matches_df = load_model_data()
    
    if len(matches_df) > 0:
        mu, home_adv_dict, attack_dict, defense_dict, teams_list, leagues_list = fit_prediction_model(matches_df)
        st.success(f"✓ Modelo listo ({len(matches_df)} partidos históricos)")
    else:
        st.error("Error al cargar datos")
        st.stop()

# Refresh button
col_refresh = st.columns([1, 10, 1])
with col_refresh[0]:
    if st.button("🔄", help="Actualizar modelo con datos nuevos"):
        st.cache_data.clear()
        st.rerun()

# Load upcoming matches
upcoming_matches = get_upcoming_matches_from_file(str(PROJECT_ROOT / "temp_parser_all.py"))

# Filters
col1, col2 = st.columns(2)

with col1:
    if len(upcoming_matches) > 0:
        selected_league = get_accent_insensitive_selectbox(
            "🏆 Selecciona una liga",
            sorted(upcoming_matches['league'].unique().tolist()),
            key="league_filter"
        )
    else:
        selected_league = st.selectbox("🏆 Selecciona una liga", leagues_list, key="league_fallback")

with col2:
    if len(upcoming_matches) > 0 and selected_league:
        # Get jornadas for the selected league
        league_matches_for_filter = upcoming_matches[upcoming_matches['league'] == selected_league]
        available_jornadas = sorted(league_matches_for_filter['jornada'].unique().tolist())
        
        if available_jornadas:
            selected_jornada = st.selectbox(
                "📅 Selecciona la jornada",
                available_jornadas,
                key="jornada_filter",
                format_func=lambda x: f"Jornada {x}"
            )
        else:
            selected_jornada = None
    else:
        selected_jornada = None

st.markdown("---")

# ============================================================================
# DISPLAY PREDICTIONS
# ============================================================================

if len(upcoming_matches) > 0 and selected_league and selected_jornada:
    # Filter by league AND jornada
    filtered_matches = upcoming_matches[
        (upcoming_matches['league'] == selected_league) & 
        (upcoming_matches['jornada'] == selected_jornada)
    ].reset_index(drop=True)
    
    if len(filtered_matches) > 0:
        st.markdown(f"### ⚽ {selected_league} - Jornada {selected_jornada}")
        st.markdown(f"**{len(filtered_matches)} partidos**")
        st.markdown("")
        
        for idx, match in filtered_matches.iterrows():
            home = match['home_team']
            away = match['away_team']
            
            # Make prediction
            pred = predict_match(home, away, selected_league, mu, home_adv_dict, attack_dict, defense_dict)
            
            # Display
            st.markdown(f"""
                <div class="prediction-row">
                    <div class="match-info">
                        <div class="match-teams">{home} <span style="opacity: 0.6;">vs</span> {away}</div>
                        <div class="match-meta">
                            📍 Jornada {match['jornada']} · 
                            🕐 {match['date']} {match['time']}
                        </div>
                    </div>
                    <div class="prediction-odds">
                        <div class="odd-box odd-box-home">
                            <strong>{pred['home_prob']:.0f}%</strong><br>
                            <span class="odd-prob">{pred['home_odds']:.2f}</span>
                        </div>
                        <div class="odd-box odd-box-draw">
                            <strong>{pred['draw_prob']:.0f}%</strong><br>
                            <span class="odd-prob">{pred['draw_odds']:.2f}</span>
                        </div>
                        <div class="odd-box odd-box-away">
                            <strong>{pred['away_prob']:.0f}%</strong><br>
                            <span class="odd-prob">{pred['away_odds']:.2f}</span>
                        </div>
                    </div>
                </div>
            """, unsafe_allow_html=True)
            
            # Show xG on hover/expand
            with st.expander(f"📊 xG: {home} {pred['xg_home']:.2f} - {pred['xg_away']:.2f} {away}", expanded=False):
                col_a, col_b, col_c = st.columns(3)
                with col_a:
                    st.metric(f"Ataque {home}", f"{attack_dict.get(home, 0):.3f}")
                with col_b:
                    st.metric(f"Home Adv", f"{np.exp(home_adv_dict.get(selected_league, 0)):.3f}")
                with col_c:
                    st.metric(f"Ataque {away}", f"{attack_dict.get(away, 0):.3f}")
    else:
        st.info(f"No hay partidos en {selected_league} Jornada {selected_jornada}")
elif len(upcoming_matches) > 0:
    st.info("👆 Selecciona una liga y jornada para ver predicciones")
else:
    st.warning("⚠️ No se pudieron cargar los partidos próximos. Asegúrate de que temp_parser_all.py existe.")

st.divider()

with st.expander("📖 Sobre las predicciones"):
    st.markdown("""
        **Modelo**: Poisson Dixon-Coles
        - Home advantage específico por liga
        - Ataque y defensa por equipo
        - Time decay (últimas 2 semanas pesan más)
        
        **Formato de cuotas**: Europeo (1/probabilidad)
        
        **Próximas mejoras**:
        - API integrada para calendarios automáticos
        - Actualización semanal del modelo
        - Histórico de predicciones vs resultados
    """)
