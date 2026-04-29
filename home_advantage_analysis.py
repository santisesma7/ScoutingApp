"""
Home Advantage Analysis for Dixon-Coles Model
Analyzes what the European league data tells us about home/away impact
"""

from pathlib import Path
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import poisson

# Setup paths
PROJECT_ROOT = Path(__file__).parent
DATA_PATH = PROJECT_ROOT / "event_data" / "processed" / "top5_events_current.parquet"

# Load match data
print("Loading match data...")
df = pd.read_parquet(DATA_PATH)

matches_data = []
for match_id in df['matchId'].unique():
    match_events = df[df['matchId'] == match_id]
    teams = match_events['team_name'].unique()
    
    if len(teams) >= 2:
        team1, team2 = sorted(teams)[:2]
        first_row = match_events.iloc[0]
        match_date = pd.to_datetime(first_row['match_date'])
        league = first_row['league']
        season = first_row['season']
        
        team1_events = match_events[match_events['team_name'] == team1]
        team2_events = match_events[match_events['team_name'] == team2]
        
        goals1 = ((team1_events['Event Type'] == 'Goal') | (team1_events['LeadingToGoal'] == True)).sum()
        goals2 = ((team2_events['Event Type'] == 'Goal') | (team2_events['LeadingToGoal'] == True)).sum()
        
        team1_id = team1_events['Team ID'].iloc[0] if len(team1_events) > 0 else None
        team2_id = team2_events['Team ID'].iloc[0] if len(team2_events) > 0 else None
        
        matches_data.append({
            'matchId': match_id,
            'team1_name': team1,
            'team2_name': team2,
            'team1_id': team1_id,
            'team2_id': team2_id,
            'goals1': int(goals1),
            'goals2': int(goals2),
            'league': league,
            'season': season,
            'match_date': match_date,
        })

all_matches = pd.DataFrame(matches_data)
print(f"Loaded {len(all_matches):,} matches total")
print(f"Leagues: {sorted(all_matches['league'].unique().tolist())}")

# ============================================================================
# HOME ADVANTAGE ANALYSIS
# ============================================================================

print("\n" + "=" * 80)
print("HOME ADVANTAGE BY LEAGUE (what the European data shows us)")
print("=" * 80)

home_stats = all_matches.groupby('league').agg({
    'goals1': ['count', 'mean'],  # home goals
    'goals2': ['mean'],            # away goals
}).round(3)
home_stats.columns = ['matches', 'avg_home_goals', 'avg_away_goals']

# Calculate home wins vs away wins by league
all_matches['result'] = all_matches.apply(
    lambda row: 'home_win' if row['goals1'] > row['goals2'] 
                else 'away_win' if row['goals2'] > row['goals1'] 
                else 'draw', axis=1
)

home_advantage = all_matches.groupby('league')['result'].value_counts().unstack(fill_value=0)
home_advantage['home_win_pct'] = home_advantage['home_win'] / (home_advantage['home_win'] + home_advantage['away_win'] + home_advantage['draw']) * 100

home_combined = pd.concat([home_stats, home_advantage[['home_win_pct']]], axis=1)
home_combined = home_combined.sort_values('matches', ascending=False)
print(home_combined.to_string())

print("\n" + "=" * 80)
print("OVERALL HOME ADVANTAGE (all leagues combined)")
print("=" * 80)
overall_home_goals = all_matches['goals1'].mean()
overall_away_goals = all_matches['goals2'].mean()
overall_home_wins = (all_matches['goals1'] > all_matches['goals2']).sum()
overall_draws = (all_matches['goals1'] == all_matches['goals2']).sum()
overall_away_wins = (all_matches['goals2'] > all_matches['goals1']).sum()
total_matches_calc = len(all_matches)

print(f"Average goals scored AT HOME: {overall_home_goals:.3f}")
print(f"Average goals scored AWAY:    {overall_away_goals:.3f}")
print(f"Home advantage (goal difference): {overall_home_goals - overall_away_goals:.3f} goals/match")
print(f"\nHome wins: {overall_home_wins} ({overall_home_wins/total_matches_calc*100:.1f}%)")
print(f"Draws:     {overall_draws} ({overall_draws/total_matches_calc*100:.1f}%)")
print(f"Away wins: {overall_away_wins} ({overall_away_wins/total_matches_calc*100:.1f}%)")

# ============================================================================
# FIT MODELS WITH AND WITHOUT HOME ADVANTAGE PARAMETER
# ============================================================================

def fit_poisson_model(matches):
    """Fit Poisson model WITHOUT home advantage"""
    teams = set(matches['team1_name']) | set(matches['team2_name'])
    team_list = sorted(list(teams))
    team_idx = {team: i for i, team in enumerate(team_list)}
    
    n_teams = len(team_list)
    params = np.concatenate([
        [np.log(1.0)],  # mu
        np.zeros(n_teams),  # attack
        np.zeros(n_teams),  # defense
    ])
    
    def log_likelihood(params):
        mu = params[0]
        attack = params[1:1+n_teams]
        defense = params[1+n_teams:]
        
        ll = 0
        for _, row in matches.iterrows():
            i, j = team_idx[row['team1_name']], team_idx[row['team2_name']]
            lambda1 = np.exp(mu + attack[i] + defense[j])
            lambda2 = np.exp(mu + attack[j] + defense[i])
            
            ll -= poisson.logpmf(int(row['goals1']), lambda1) + poisson.logpmf(int(row['goals2']), lambda2)
        return ll
    
    result = minimize(log_likelihood, params, method='BFGS')
    
    mu = result.x[0]
    attack_dict = {team_list[i]: result.x[1+i] for i in range(n_teams)}
    defense_dict = {team_list[i]: result.x[1+n_teams+i] for i in range(n_teams)}
    
    return mu, attack_dict, defense_dict, result.fun

def fit_poisson_with_home_advantage(matches):
    """Fit Poisson model WITH home advantage parameter"""
    teams = set(matches['team1_name']) | set(matches['team2_name'])
    team_list = sorted(list(teams))
    team_idx = {team: i for i, team in enumerate(team_list)}
    
    n_teams = len(team_list)
    params = np.concatenate([
        [np.log(1.0)],  # mu
        [np.log(1.05)],  # home_advantage parameter (start at ~5%)
        np.zeros(n_teams),  # attack
        np.zeros(n_teams),  # defense
    ])
    
    def log_likelihood(params):
        mu = params[0]
        home_adv = params[1]
        attack = params[2:2+n_teams]
        defense = params[2+n_teams:]
        
        ll = 0
        for _, row in matches.iterrows():
            i, j = team_idx[row['team1_name']], team_idx[row['team2_name']]
            # Home team advantage added here
            lambda1 = np.exp(mu + home_adv + attack[i] + defense[j])
            lambda2 = np.exp(mu + attack[j] + defense[i])
            
            ll -= poisson.logpmf(int(row['goals1']), lambda1) + poisson.logpmf(int(row['goals2']), lambda2)
        return ll
    
    result = minimize(log_likelihood, params, method='BFGS')
    
    mu = result.x[0]
    home_adv = result.x[1]
    attack_dict = {team_list[i]: result.x[2+i] for i in range(n_teams)}
    defense_dict = {team_list[i]: result.x[2+n_teams+i] for i in range(n_teams)}
    
    return mu, home_adv, attack_dict, defense_dict, result.fun

print("\n" + "=" * 80)
print("MODEL FITTING: WITH vs WITHOUT HOME ADVANTAGE PARAMETER")
print("=" * 80)

print("\nFitting model WITHOUT home advantage...")
mu_no_ha, attack_no_ha, defense_no_ha, ll_no_ha = fit_poisson_model(all_matches)

print("Fitting model WITH home advantage...")
mu_ha, home_adv_param, attack_ha, defense_ha, ll_ha = fit_poisson_with_home_advantage(all_matches)

print("\n" + "-" * 80)
print("MODEL COMPARISON")
print("-" * 80)

print(f"\nModel WITHOUT Home Advantage:")
print(f"  Log-Likelihood: {ll_no_ha:.2f}")
print(f"  Intercept (mu): {mu_no_ha:.4f}")

print(f"\nModel WITH Home Advantage:")
print(f"  Log-Likelihood: {ll_ha:.2f}")
print(f"  Intercept (mu): {mu_ha:.4f}")
print(f"  HOME ADVANTAGE PARAMETER (log scale): {home_adv_param:.4f}")
print(f"  HOME ADVANTAGE (linear scale): {np.exp(home_adv_param):.4f}")
print(f"  → This means: Home team's expected goals multiplied by {np.exp(home_adv_param):.3f}x")
print(f"  → Or: Home team gets ~{(np.exp(home_adv_param)-1)*100:.1f}% more expected goals")

ll_improvement = ll_no_ha - ll_ha
print(f"\nModel Improvement (Log-Likelihood decrease, better is lower):")
print(f"  LL difference: {ll_improvement:.2f}")
print(f"  {'✓ Model WITH home advantage is BETTER' if ll_improvement > 0 else '✗ Home advantage does NOT improve model'}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 80)
print("KEY INSIGHTS: What the European League Data Tells Us")
print("=" * 80)

print(f"""
1. HOME ADVANTAGE MAGNITUDE:
   - Home teams score {overall_home_goals:.2f} goals vs away teams scoring {overall_away_goals:.2f}
   - Difference: {overall_home_goals - overall_away_goals:.3f} goals per match
   - Home teams win {overall_home_wins/total_matches_calc*100:.1f}% of matches

2. LEAGUE DIFFERENCES (European data comparison):
""")

for league in home_combined.index:
    row = home_combined.loc[league]
    print(f"   {league:15s}: {row['avg_home_goals']:.2f} goals home vs {row['avg_away_goals']:.2f} away ({row['home_win_pct']:.1f}% home wins)")

print(f"""
3. PARAMETER IMPORTANCE:
   - Home advantage coefficient: {np.exp(home_adv_param):.4f}
   - Adding home advantage parameter {'IMPROVES' if ll_improvement > 0 else 'DOES NOT IMPROVE'} model likelihood by {abs(ll_improvement):.2f}
   - This shows home advantage IS {'a significant' if abs(ll_improvement) > 10 else 'a minor'} factor

4. WHAT THIS MEANS FOR PREDICTIONS:
   - If home advantage is important (large parameter), predictions should account for it
   - Different leagues may have different home advantage effects (shown in stats above)
   - European data provides validation that home advantage is {'consistent' if overall_home_wins/total_matches_calc*100 > 45 else 'not as pronounced'} across leagues
""")

print("=" * 80)
