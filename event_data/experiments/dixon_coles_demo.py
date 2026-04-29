from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.stats import poisson

DATA_PATH = Path("event_data/processed/top5_events_current.parquet")


def load_match_scores(path: Path = DATA_PATH) -> pd.DataFrame:
    df = pd.read_parquet(path, columns=["matchId", "league", "season", "Team ID", "team_name", "Event Type"])

    teams = (
        df[["matchId", "league", "season", "Team ID", "team_name"]]
        .drop_duplicates()
        .dropna(subset=["team_name"])
        .copy()
    )

    goals = (
        df[df["Event Type"] == "Goal"]
        .groupby(["matchId", "team_name"], as_index=False)
        .size()
        .rename(columns={"size": "goals"})
    )

    match_goals = teams.merge(goals, on=["matchId", "team_name"], how="left")
    match_goals["goals"] = match_goals["goals"].fillna(0).astype(int)
    match_goals = match_goals.sort_values(["matchId", "team_name"]).copy()

    counts = match_goals.groupby("matchId").size()
    valid_match_ids = counts[counts == 2].index
    match_goals = match_goals[match_goals["matchId"].isin(valid_match_ids)].copy()

    match_goals["side"] = match_goals.groupby("matchId").cumcount() + 1
    pivot = match_goals.pivot(
        index="matchId",
        columns="side",
        values=["team_name", "Team ID", "goals"],
    )
    pivot.columns = [f"{col}_{side}" for col, side in pivot.columns]
    pivot = pivot.reset_index()

    meta = (
        match_goals.groupby("matchId", as_index=False)[["league", "season"]]
        .first()
    )

    pivot = pivot.merge(meta, on="matchId", how="left")
    pivot = pivot.rename(
        columns={
            "team_name_1": "team1_name",
            "team_name_2": "team2_name",
            "Team ID_1": "team1_id",
            "Team ID_2": "team2_id",
            "goals_1": "goals1",
            "goals_2": "goals2",
        }
    )

    return pivot


def fit_poisson_model(matches: pd.DataFrame) -> tuple[float, dict[str, float], dict[str, float]]:
    teams = sorted(set(matches["team1_name"]).union(matches["team2_name"]))
    team_index = {team: idx for idx, team in enumerate(teams)}
    n_teams = len(teams)

    def unpack(params: np.ndarray) -> tuple[float, np.ndarray, np.ndarray]:
        mu = params[0]
        attack = np.zeros(n_teams, dtype=float)
        defense = np.zeros(n_teams, dtype=float)
        attack[1:] = params[1 : n_teams]
        defense[1:] = params[n_teams :]
        return mu, attack, defense

    match_i = matches["team1_name"].map(team_index).to_numpy(dtype=int)
    match_j = matches["team2_name"].map(team_index).to_numpy(dtype=int)
    goals_i = matches["goals1"].to_numpy(dtype=int)
    goals_j = matches["goals2"].to_numpy(dtype=int)

    def objective(params: np.ndarray) -> float:
        mu, attack, defense = unpack(params)
        lam_i = np.exp(mu + attack[match_i] + defense[match_j])
        lam_j = np.exp(mu + attack[match_j] + defense[match_i])
        nll = -poisson.logpmf(goals_i, lam_i).sum() - poisson.logpmf(goals_j, lam_j).sum()
        reg = 1e-4 * np.sum(params[1:] ** 2)
        return nll + reg

    initial = np.zeros(1 + 2 * (n_teams - 1), dtype=float)
    result = minimize(objective, initial, method="L-BFGS-B")
    if not result.success:
        raise RuntimeError(f"Poisson model optimization failed: {result.message}")

    mu, attack, defense = unpack(result.x)
    attack_map = {team: float(attack[idx]) for team, idx in team_index.items()}
    defense_map = {team: float(defense[idx]) for team, idx in team_index.items()}
    return float(mu), attack_map, defense_map


def score_matrix(lambda1: float, lambda2: float, max_goals: int = 6) -> pd.DataFrame:
    goals = np.arange(max_goals + 1)
    p1 = poisson.pmf(goals, lambda1)
    p2 = poisson.pmf(goals, lambda2)
    probs = np.outer(p1, p2)

    rows = []
    for i in goals:
        for j in goals:
            rows.append({"goals1": i, "goals2": j, "prob": float(probs[i, j])})
    return pd.DataFrame(rows)


def dixon_coles_adjustment(goals1: int, goals2: int, lambda1: float, lambda2: float, rho: float) -> float:
    if (goals1, goals2) == (0, 0):
        return 1.0 - lambda1 * lambda2 * rho
    if (goals1, goals2) == (0, 1):
        return 1.0 + lambda1 * rho
    if (goals1, goals2) == (1, 0):
        return 1.0 + lambda2 * rho
    if (goals1, goals2) == (1, 1):
        return 1.0 - rho
    return 1.0


def scoreline_probabilities(
    lambda1: float,
    lambda2: float,
    max_goals: int = 6,
    rho: float | None = None,
) -> pd.DataFrame:
    matrix = score_matrix(lambda1, lambda2, max_goals=max_goals)
    if rho is not None:
        matrix["prob"] = matrix.apply(
            lambda row: row["prob"] * dixon_coles_adjustment(
                int(row["goals1"]),
                int(row["goals2"]),
                lambda1,
                lambda2,
                rho,
            ),
            axis=1,
        )
        matrix["prob"] = matrix["prob"].clip(lower=0.0)
    matrix["prob"] /= matrix["prob"].sum()
    return matrix


def fit_dixon_coles_rho(
    matches: pd.DataFrame,
    mu: float,
    attack_map: dict[str, float],
    defense_map: dict[str, float],
) -> float:
    teams = sorted(set(matches["team1_name"]).union(matches["team2_name"]))
    team_index = {team: idx for idx, team in enumerate(teams)}
    match_i = matches["team1_name"].map(team_index).to_numpy(dtype=int)
    match_j = matches["team2_name"].map(team_index).to_numpy(dtype=int)
    goals_i = matches["goals1"].to_numpy(dtype=int)
    goals_j = matches["goals2"].to_numpy(dtype=int)
    attack = np.array([attack_map[team] for team in teams], dtype=float)
    defense = np.array([defense_map[team] for team in teams], dtype=float)

    lambda_i = np.exp(mu + attack[match_i] + defense[match_j])
    lambda_j = np.exp(mu + attack[match_j] + defense[match_i])

    def objective(rho: np.ndarray) -> float:
        if abs(rho[0]) >= 0.95:
            return 1e8
        probs = poisson.pmf(goals_i, lambda_i) * poisson.pmf(goals_j, lambda_j)
        adjustments = np.array([
            dixon_coles_adjustment(int(g1), int(g2), lam1, lam2, rho[0])
            for g1, g2, lam1, lam2 in zip(goals_i, goals_j, lambda_i, lambda_j)
        ], dtype=float)
        adjusted = probs * adjustments
        if np.any(adjusted <= 0):
            return 1e8
        return -np.log(adjusted).sum()

    result = minimize(objective, x0=[0.05], bounds=[(-0.95, 0.95)], method="L-BFGS-B")
    if not result.success:
        raise RuntimeError(f"Dixon-Coles rho optimization failed: {result.message}")
    return float(result.x[0])


def summarize_low_score_frequencies(
    matches: pd.DataFrame,
    mu: float,
    attack_map: dict[str, float],
    defense_map: dict[str, float],
    rho: float | None = None,
) -> pd.DataFrame:
    teams = sorted(set(matches["team1_name"]).union(matches["team2_name"]))
    team_index = {team: idx for idx, team in enumerate(teams)}
    match_i = matches["team1_name"].map(team_index).to_numpy(dtype=int)
    match_j = matches["team2_name"].map(team_index).to_numpy(dtype=int)
    goals_i = matches["goals1"].to_numpy(dtype=int)
    goals_j = matches["goals2"].to_numpy(dtype=int)
    attack = np.array([attack_map[team] for team in teams], dtype=float)
    defense = np.array([defense_map[team] for team in teams], dtype=float)

    lambda_i = np.exp(mu + attack[match_i] + defense[match_j])
    lambda_j = np.exp(mu + attack[match_j] + defense[match_i])

    actual = (
        matches[["goals1", "goals2"]]
        .value_counts()
        .rename("actual_count")
        .reset_index()
    )

    predicted = []
    for lam1, lam2 in zip(lambda_i, lambda_j):
        scores = scoreline_probabilities(lam1, lam2, max_goals=5, rho=rho)
        predicted.append(scores)

    predicted_df = pd.concat(predicted, ignore_index=True)
    predicted = (
        predicted_df.groupby(["goals1", "goals2"])["prob"].sum().reset_index()
    )
    predicted = predicted.rename(columns={"prob": "predicted_sum"})

    report = actual.merge(predicted, on=["goals1", "goals2"], how="outer").fillna(0)
    report = report.sort_values(["goals1", "goals2"]).reset_index(drop=True)
    report["predicted_share"] = report["predicted_sum"] / report["predicted_sum"].sum()
    report["actual_share"] = report["actual_count"] / report["actual_count"].sum()
    return report


def main() -> None:
    print("Loading event data and building match scores...")
    matches = load_match_scores()
    print(f"Loaded {len(matches):,} matches from {DATA_PATH}")
    print(f"Leagues: {matches['league'].nunique()}, seasons: {matches['season'].nunique()}\n")

    sample_matches = matches["league"].value_counts().head(5)
    print("Top leagues by match count:")
    print(sample_matches.to_string(), "\n")

    print("Fitting Poisson attack/defense model...")
    mu, attack_map, defense_map = fit_poisson_model(matches)
    print(f"  intercept mu = {mu:.4f}")

    team_scores = pd.DataFrame(
        {
            "team_name": list(attack_map.keys()),
            "attack": list(attack_map.values()),
            "defense": list(defense_map.values()),
        }
    )
    team_scores["attack_minus_defense"] = team_scores["attack"] - team_scores["defense"]
    print("\nTop attack strengths:")
    print(team_scores.sort_values("attack", ascending=False).head(10).to_string(index=False))
    print("\nTop defense strengths (smaller is stronger):")
    print(team_scores.sort_values("defense").head(10).to_string(index=False))

    sample_match = matches.iloc[-1]
    print("\nSample match for prediction:")
    print(sample_match[["matchId", "league", "season", "team1_name", "team2_name", "goals1", "goals2"]].to_string())

    lam1 = np.exp(mu + attack_map[sample_match["team1_name"]] + defense_map[sample_match["team2_name"]])
    lam2 = np.exp(mu + attack_map[sample_match["team2_name"]] + defense_map[sample_match["team1_name"]])
    print(f"Expected goals: {sample_match['team1_name']}={lam1:.2f}, {sample_match['team2_name']}={lam2:.2f}")

    probs = scoreline_probabilities(lam1, lam2, max_goals=5)
    print("\nTop 6 predicted scorelines without Dixon-Coles:")
    print(probs.sort_values("prob", ascending=False).head(6).to_string(index=False))

    print("\nFitting Dixon-Coles rho parameter on low-score adjustments...")
    rho = fit_dixon_coles_rho(matches, mu, attack_map, defense_map)
    print(f"  fitted rho = {rho:.4f}\n")

    dc_probs = scoreline_probabilities(lam1, lam2, max_goals=5, rho=rho)
    print("Top 6 scorelines with Dixon-Coles:")
    print(dc_probs.sort_values("prob", ascending=False).head(6).to_string(index=False))

    print("\nComparing actual vs predicted shares for low scorelines:")
    report_baseline = summarize_low_score_frequencies(matches, mu, attack_map, defense_map, rho=None)
    report_dc = summarize_low_score_frequencies(matches, mu, attack_map, defense_map, rho=rho)
    merged = report_baseline.merge(
        report_dc[["goals1", "goals2", "predicted_share"]],
        on=["goals1", "goals2"],
        how="left",
        suffixes=("_base", "_dc"),
    )
    print(merged.head(12).to_string(index=False))

    print("\nDemo complete. The script fits a Poisson model and shows how Dixon-Coles changes low-score prediction share.")


if __name__ == "__main__":
    main()
