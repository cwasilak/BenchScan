import csv
from collections import Counter
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"

DETAIL_FILE = DATA_DIR / "Inventory_Detail.csv"
SUMMARY_FILE = DATA_DIR / "Inventory_Summary.csv"


def build_summary():

    if not DETAIL_FILE.exists():
        return

    counter = Counter()

    with open(DETAIL_FILE, newline="", encoding="utf-8") as f:

        reader = csv.DictReader(f)

        for row in reader:

            key = (
                row["Manufacturer"],
                row["Model"],
                row["CPU"],
                row["RAM"],
                row["Storage Size"],
                row["Storage Type"],
                row.get("Battery Present", "")
            )

            counter[key] += 1

    with open(SUMMARY_FILE, "w", newline="", encoding="utf-8") as f:

        writer = csv.writer(f)

        writer.writerow([
            "Qty",
            "Manufacturer",
            "Model",
            "CPU",
            "RAM",
            "Storage Size",
            "Storage Type",
            "Battery Present"
        ])

        for key in sorted(counter.keys()):

            qty = counter[key]

            writer.writerow([
                qty,
                *key
            ])