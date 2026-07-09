from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]

LOCAL_DATA = PROJECT_ROOT / "data"

EXPORT_LOCATIONS = [
    Path("/media/user/BENCHSCAN_DATA"),
    Path("/mnt/BENCHSCAN_DATA"),
    LOCAL_DATA,
]


def get_data_dir():

    for path in EXPORT_LOCATIONS:
        if path.exists() and path.is_dir():
            return path

    LOCAL_DATA.mkdir(exist_ok=True)
    return LOCAL_DATA


DATA_DIR = get_data_dir()

DETAIL_FILE = DATA_DIR / "Inventory_Detail.csv"
SUMMARY_FILE = DATA_DIR / "Inventory_Summary.csv"