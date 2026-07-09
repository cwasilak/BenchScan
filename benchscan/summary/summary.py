import csv
from collections import Counter

from benchscan.paths import DETAIL_FILE, SUMMARY_FILE


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
                row.get("Battery Present", ""),
                row.get("Notes", "")
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
            "Battery Present",
            "Notes"
        ])

        for key in sorted(counter.keys()):

            writer.writerow([
                counter[key],
                *key
            ])