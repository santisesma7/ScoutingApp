import os
import requests
from pathlib import Path

DATA_FILES = {
    "event_data/processed/player_metrics_enriched.parquet": "https://drive.google.com/uc?id=1dhUUKplP9jHM5tJRo5n2M9pqC9gwaIiG",
    "event_data/processed/team_metrics.parquet": "https://drive.google.com/uc?id=1Zk7X5AVTs6P2HBzLC-NrnacRN1hYVQQ4",
    "event_data/processed/events.duckdb": "https://drive.google.com/uc?id=1mFq2sdc8NE4sA-ByuzKyNT8d0zur-z9p",
}

def download_file(url, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    if output_path.exists():
        return

    print(f"Descargando {output_path.name}...")

    response = requests.get(url, stream=True)
    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

def ensure_data_files():
    for path_str, url in DATA_FILES.items():
        path = Path(path_str)
        download_file(url, path)