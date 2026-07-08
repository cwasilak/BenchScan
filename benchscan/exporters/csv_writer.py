import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

CSV_FILE = DATA_DIR / "Inventory_Detail.csv"

HEADERS = [
    "Scan Date",
    "Manufacturer",
    "Model",
    "Serial Number",
    "CPU",
    "RAM",
    "Storage Size",
    "Storage Type",
    "Storage Model"
]


def inventory_to_row(inventory):
    return {
        "Scan Date": inventory.scan_date,
        "Manufacturer": inventory.manufacturer,
        "Model": inventory.model,
        "Serial Number": inventory.serial,
        "CPU": inventory.cpu,
        "RAM": f"{inventory.ram_gb} GB",
        "Storage Size": inventory.storage_size,
        "Storage Type": inventory.storage_type,
        "Storage Model": inventory.storage_model,
    }


def write_inventory(inventory):

    rows = []

    if CSV_FILE.exists():
        with open(CSV_FILE, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))

    new_row = inventory_to_row(inventory)

    updated = False

    for i, row in enumerate(rows):
        if row.get("Serial Number") == inventory.serial:
            rows[i] = new_row
            updated = True
            break

    if not updated:
        rows.append(new_row)

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=HEADERS)

        writer.writeheader()

        writer.writerows(rows)