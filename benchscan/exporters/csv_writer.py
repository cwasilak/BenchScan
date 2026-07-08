import csv
from pathlib import Path

# Project root (BenchScan/)
PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

CSV_FILE = DATA_DIR / "Inventory_Detail.csv"


def write_inventory(inventory):

    file_exists = CSV_FILE.exists()

    with open(CSV_FILE, "a", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        if not file_exists:
            writer.writerow([
                "Scan Date",
                "Manufacturer",
                "Model",
                "Serial Number",
                "CPU",
                "RAM",
                "Storage Size",
                "Storage Type",
                "Storage Model"
            ])

        writer.writerow([
            inventory.scan_date,
            inventory.manufacturer,
            inventory.model,
            inventory.serial,
            inventory.cpu,
            f"{inventory.ram_gb} GB",
            inventory.storage_size,
            inventory.storage_type,
            inventory.storage_model
        ])