from pathlib import Path
import pandas as pd
import streamlit as st
import duckdb

PLAYER_METRICS_PATH = Path("event_data/processed/player_metrics_enriched.parquet")
TEAM_METRICS_PATH = Path("event_data/processed/team_metrics.parquet")
DUCKDB_PATH = Path("event_data/processed/events.duckdb")


@st.cache_data
def load_player_metrics():
    if not PLAYER_METRICS_PATH.exists():
        raise FileNotFoundError(f"No se encontró {PLAYER_METRICS_PATH}")
    return pd.read_parquet(PLAYER_METRICS_PATH)


@st.cache_data
def load_team_metrics():
    if not TEAM_METRICS_PATH.exists():
        raise FileNotFoundError(f"No se encontró {TEAM_METRICS_PATH}")
    return pd.read_parquet(TEAM_METRICS_PATH)


def query_events(sql: str) -> pd.DataFrame:
    if not DUCKDB_PATH.exists():
        raise FileNotFoundError(f"No se encontró {DUCKDB_PATH}")

    con = duckdb.connect(str(DUCKDB_PATH), read_only=True)
    try:
        return con.execute(sql).df()
    finally:
        con.close()