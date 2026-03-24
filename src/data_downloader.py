import requests
from pathlib import Path

# URLs de Drive
PLAYER_URL = "https://drive.google.com/uc?id=1dhUUKplP9jHM5tJRo5n2M9pqC9gwaIiG"
TEAM_URL = "https://drive.google.com/uc?id=1Zk7X5AVTs6P2HBzLC-NrnacRN1hYVQQ4"
EVENTS_URL = "https://drive.google.com/uc?id=1mFq2sdc8NE4sA-ByuzKyNT8d0zur-z9p"
VERSION_URL = "https://drive.google.com/uc?id=1tvP74Z_w9D0o9SxcmqslcsuZesjJdgo4"

# Rutas locales
PLAYER_PATH = Path("event_data/processed/player_metrics_enriched.parquet")
TEAM_PATH = Path("event_data/processed/team_metrics.parquet")
EVENTS_PATH = Path("event_data/processed/events.duckdb")
LOCAL_VERSION_PATH = Path("event_data/processed/data_version.txt")


def download_file(url, output_path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(output_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)


def get_remote_version():
    try:
        response = requests.get(VERSION_URL)
        response.raise_for_status()
        return response.text.strip()
    except:
        return None


def get_local_version():
    if LOCAL_VERSION_PATH.exists():
        return LOCAL_VERSION_PATH.read_text().strip()
    return None


def save_local_version(version):
    LOCAL_VERSION_PATH.parent.mkdir(parents=True, exist_ok=True)
    LOCAL_VERSION_PATH.write_text(version)


def ensure_data_files():

    remote_version = get_remote_version()
    local_version = get_local_version()

    # 🔥 SI LA VERSIÓN CAMBIA → BORRAR TODO
    if remote_version is not None and remote_version != local_version:
        print("🔄 Nueva versión detectada. Re-descargando datos...")

        for path in [PLAYER_PATH, TEAM_PATH, EVENTS_PATH]:
            if path.exists():
                path.unlink()

    # Descargar si no existen
    if not PLAYER_PATH.exists():
        download_file(PLAYER_URL, PLAYER_PATH)

    if not TEAM_PATH.exists():
        download_file(TEAM_URL, TEAM_PATH)

    if not EVENTS_PATH.exists():
        download_file(EVENTS_URL, EVENTS_PATH)

    # Guardar versión
    if remote_version is not None:
        save_local_version(remote_version)