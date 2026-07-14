import platform
import subprocess
import sys

from benchscan.paths import DATA_DIR, USB_DATA_DIR
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

    if DATA_DIR == USB_DATA_DIR:
        print("✓ Export Location")
        print()
        return

    print("✗ Export Location")
    print()
    print("=" * 60)
    print("ERROR")
    print("=" * 60)
    print()
    print("BENCHDATA partition not found.")
    print("Inventory cannot be saved.")
    print("Please verify the USB data partition is mounted.")
    print()

    input("Press ENTER to shut down...")

    if platform.system() == "Linux":
        subprocess.run(["sudo", "poweroff"])

    sys.exit(1)