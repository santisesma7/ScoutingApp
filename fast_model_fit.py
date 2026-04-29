"""
Fast Poisson + Home Advantage + Time Decay Model
Uses better optimization strategies for speed
"""

from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import poisson

PROJECT_ROOT = Path.cwd()
if not (PROJECT_ROOT / "event_data").exists():
    PROJECT_ROOT = PROJECT_ROOT.parent

DATA_PATH = PROJECT_ROOT / "event_data" / "processed" / "top5_events_current.parquet"

# ============================================================================
# FAST IMPLEMENTATION
# ============================================================================

def compute_time_decay_weights(matches, half_life_days=90):
    """Exponential time decay weights"""
    max_date = matches['match_date'].max()
    days_ago = (max_date - matches['match_date']).dt.days.values
    return 2.0 ** (-days_ago / half_life_days)

def fit_poisson_fast(matches, use_home_advantage=True, use_time_decay=True):
    """
    FAST Poisson model fit using better optimization strategy
    """
    teams = sorted(list(set(matches['team1_name']) | set(matches['team2_name'])))
    team_idx = {team: i for i, team in enumerate(teams)}
    n_teams = len(teams)
    
    # Pre-compute indices and goals (vectorized)
    team1_idx = np.array([team_idx[t] for t in matches['team1_name']], dtype=int)
    team2_idx = np.array([team_idx[t] for t in matches['team2_name']], dtype=int)
    goals1 = matches['goals1'].values.astype(int)
    goals2 = matches['goals2'].values.astype(int)
    
    weights = compute_time_decay_weights(matches) if use_time_decay else np.ones(len(matches))
    
    # Initial parameters
    n_params = (4 if use_home_advantage else 3) + 2 * n_teams
    x0 = np.random.normal(0, 0.05, n_params)
    if use_home_advantage:
        x0[1] = 0.05  # Home advantage ~5%
    
    def neg_ll(x):
        """Negative log-likelihood (vectorized)"""
        mu = x[0]
        offset = 1 if use_home_advantage else 0
        home_adv = x[1] if use_home_advantage else 0.0
        attack = x[1+offset:1+offset+n_teams]
        defense = x[1+offset+n_teams:]
        
        lambda1 = np.exp(mu + home_adv + attack[team1_idx] + defense[team2_idx])
        lambda2 = np.exp(mu + attack[team2_idx] + defense[team1_idx])
        
        ll = poisson.logpmf(goals1, lambda1) + poisson.logpmf(goals2, lambda2)
        return -np.sum(weights * ll)
    
    print("Fitting model... (using fast L-BFGS-B optimizer)")
    result = minimize(neg_ll, x0, method='L-BFGS-B', 
                     options={'maxiter': 100, 'ftol': 1e-4, 'disp': False})
    
    print(f"✓ Converged in {result.nit} iterations (success={result.success})")
    
    # Extract parameters
    x = result.x
    mu = x[0]
    offset = 1 if use_home_advantage else 0
    home_adv = x[1] if use_home_advantage else None
    attack = {teams[i]: x[1+offset+i] for i in range(n_teams)}
    defense = {teams[i]: x[1+offset+n_teams+i] for i in range(n_teams)}
    
    return mu, home_adv, attack, defense

# ============================================================================
# LOAD AND FIT
# ============================================================================

print("Loading data...")
df = pd.read_parquet(DATA_PATH)

matches_list = []
for mid in df['matchId'].unique():
    match_df = df[df['matchId'] == mid]
    teams = sorted(match_df['team_name'].unique())[:2]
    if len(teams) == 2:
        t1_data = match_df[match_df['team_name'] == teams[0]].iloc[0]
        t2_data = match_df[match_df['team_name'] == teams[1]].iloc[0]
        
        goals1 = ((match_df[match_df['team_name'] == teams[0]]['Event Type'] == 'Goal').sum())
        goals2 = ((match_df[match_df['team_name'] == teams[1]]['Event Type'] == 'Goal').sum())
        
        matches_list.append({
            'matchId': mid,
            'team1_name': teams[0],
            'team2_name': teams[1],
            'goals1': int(goals1),
            'goals2': int(goals2),
            'league': t1_data['league'],
            'match_date': pd.to_datetime(t1_data['match_date']),
        })

all_matches = pd.DataFrame(matches_list)
print(f"✓ Loaded {len(all_matches)} matches\n")

# Fit models
print("=" * 80)
print("BASE MODEL (no home advantage, equal weights)")
print("=" * 80)
mu_base, _, attack_base, defense_base = fit_poisson_fast(
    all_matches, use_home_advantage=False, use_time_decay=False
)
print(f"μ = {mu_base:.4f}")

print("\n" + "=" * 80)
print("ENHANCED MODEL (with home advantage + time decay)")
print("=" * 80)
mu_enh, home_adv, attack_enh, defense_enh = fit_poisson_fast(
    all_matches, use_home_advantage=True, use_time_decay=True
)
print(f"μ = {mu_enh:.4f}")
print(f"Home advantage = {np.exp(home_adv):.4f} ({(np.exp(home_adv)-1)*100:.1f}% boost)")

print("\n" + "=" * 80)
print("TOP TEAMS (Enhanced Model)")
print("=" * 80)
teams = list(attack_enh.keys())
strengths = [(t, attack_enh[t] - defense_enh[t]) for t in teams]
strengths.sort(key=lambda x: x[1], reverse=True)

for i, (team, strength) in enumerate(strengths[:10], 1):
    print(f"{i:2d}. {team:20s} {strength:+.4f}")

print("\n✓ Model fitting complete!")
