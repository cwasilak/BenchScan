from benchscan.paths import DATA_DIR
from benchscan.logger import LOG_FILE


def check():

    print("Checking Environment...")
    print()

    if DATA_DIR.exists():
        print("✓ Data Directory")
    else:
        print("✗ Data Directory")

    if LOG_FILE.parent.exists():
        print("✓ Log Location")
    else:
        print("✗ Log Location")

    if "BENCHSCAN_DATA" in str(DATA_DIR):
        print("✓ Export Location")
    else:
        print("✓ Export Location (Local)")

    print()