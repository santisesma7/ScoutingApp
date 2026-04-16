import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler


def get_similar_players(
    df_all: pd.DataFrame,
    player_row: pd.Series,
    position_group: str,
    key_metrics: list[str],
    min_minutes_pct: float = 0.30,
    top_n: int = 10,
    use_expanded_metrics: bool = True,
) -> pd.DataFrame:
    """
    Find similar players based on Euclidean distance on key metrics.
    
    Parameters:
    -----------
    df_all : pd.DataFrame
        Full player metrics dataframe
    player_row : pd.Series
        Row of the selected player
    position_group : str
        Position group to filter by
    key_metrics : list[str]
        List of metrics to use for similarity calculation (if use_expanded_metrics=False)
    min_minutes_pct : float
        Minimum minutes as percentage of selected player (0.30 = 30%)
    top_n : int
        Number of similar players to return
    use_expanded_metrics : bool
        If True, use expanded set of metrics for better similarity; if False, use key_metrics only
        
    Returns:
    --------
    pd.DataFrame
        DataFrame with top_n similar players, sorted by distance (ascending)
    """
    
    # Filter by position
    df_pos = df_all[df_all["position_group"] == position_group].copy()
    
    # Get selected player's minutes
    player_minutes = player_row.get("minutes_total", 0)
    min_minutes_threshold = player_minutes * min_minutes_pct
    
    # Filter by minutes
    df_pos = df_pos[df_pos["minutes_total"] >= min_minutes_threshold].copy()
    
    # Exclude the selected player
    df_pos = df_pos[
        (df_pos["player_name"] != player_row["player_name"]) |
        (df_pos["team_name"] != player_row["team_name"])
    ].copy()
    
    # Determine metrics to use
    if use_expanded_metrics:
        # Expanded metrics by position - include more relevant metrics for better similarity
        expanded_metrics = {
            "Midfielder": [
                "passes_90", "successful_passes_90", "passes_final_third_90", "passes_final_third_pct",
                "pass_accuracy", "progressive_passes_90", "progressive_passes_final_third_90", "progressive_pass_pct",
                "key_passes_90", "crosses_90", "cross_accuracy", "shots_90", "goals_90", "shots_on_target_90",
                "recoveries_90", "recoveries_def_third_90", "recoveries_mid_third_90", "recoveries_final_third_90",
                "tackles_90", "tackle_success_pct", "interceptions_90", "takeons_90", "takeon_success_pct",
                "dispossessed_90", "long_pass_pct", "avg_pass_length"
            ],
            "Center Back": [
                "passes_90", "successful_passes_90", "passes_final_third_90", "passes_final_third_pct",
                "pass_accuracy", "progressive_passes_90", "progressive_pass_pct", "long_pass_pct",
                "clearances_90", "interceptions_90", "aerials_90", "aerial_win_pct", "recoveries_90",
                "recoveries_def_third_90", "recoveries_mid_third_90", "tackles_90", "tackle_success_pct",
                "blocked_passes_90", "avg_pass_length"
            ],
            "Striker": [
                "shots_90", "goals_90", "shots_on_target_90", "big_chances_90", "big_chances_created_90",
                "shot_accuracy", "goal_conversion", "inside_box_shot_pct", "shots_inside_box_90",
                "avg_shot_distance_m", "aerials_90", "aerial_win_pct", "key_passes_90", "takeons_90",
                "takeon_success_pct", "recoveries_90", "recoveries_final_third_90"
            ],
            "Winger": [
                "shots_90", "goals_90", "shots_on_target_90", "takeons_90", "takeon_success_pct",
                "key_passes_90", "crosses_90", "cross_accuracy", "big_chances_created_90",
                "progressive_passes_90", "progressive_pass_pct", "recoveries_90", "recoveries_final_third_90",
                "dispossessed_90", "passes_final_third_90", "passes_final_third_pct"
            ],
            "Full Back": [
                "progressive_pass_pct", "crosses_90", "cross_accuracy", "key_passes_90", "takeons_90",
                "takeon_success_pct", "tackles_90", "tackle_success_pct", "interceptions_90",
                "recoveries_90", "recoveries_def_third_90", "recoveries_mid_third_90", "passes_90",
                "passes_final_third_90", "passes_final_third_pct", "pass_accuracy", "progressive_passes_90"
            ],
        }
        metrics_to_use = expanded_metrics.get(position_group, key_metrics)
        # Filter to only metrics that exist in the dataframe
        metrics_to_use = [m for m in metrics_to_use if m in df_pos.columns]
        # Ensure key_metrics are included for display
        all_metrics_needed = list(set(metrics_to_use + key_metrics))
        metrics_to_use = [m for m in all_metrics_needed if m in df_pos.columns]
    else:
        metrics_to_use = key_metrics
    
    # Select only rows with all required metrics
    df_pos = df_pos.dropna(subset=metrics_to_use).copy()
    
    if df_pos.empty:
        return pd.DataFrame()
    
    # Extract and normalize metrics
    X_ref = player_row[metrics_to_use].values.reshape(1, -1)  # Selected player
    X_candidates = df_pos[metrics_to_use].values  # All candidates
    
    # Normalize together
    all_X = np.vstack([X_ref, X_candidates])
    scaler = StandardScaler()
    all_X_scaled = scaler.fit_transform(all_X)
    
    X_ref_scaled = all_X_scaled[0]
    X_candidates_scaled = all_X_scaled[1:]
    
    # Calculate Euclidean distance
    distances = np.sqrt(np.sum((X_candidates_scaled - X_ref_scaled) ** 2, axis=1))
    
    df_pos["similarity_distance"] = distances
    
    # Sort and return top_n
    result = (
        df_pos[["player_name", "team_name", "league", "season", "position_group", 
                 "minutes_total", "cluster_name", "similarity_distance", "age"]]
        .sort_values("similarity_distance")
        .head(top_n)
        .reset_index(drop=True)
    )
    
    return result
