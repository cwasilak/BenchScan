import csv
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]

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
    "Storage Model",

    "Battery Present",
    "Battery Manufacturer",
    "Battery Model",
    "Battery Design Capacity",
    "Battery Full Capacity",
    "Battery Health %",
    "Battery Cycle Count",
    "Battery Status",

    "Notes"
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

        "Battery Present": inventory.battery_present,
        "Battery Manufacturer": inventory.battery_manufacturer,
        "Battery Model": inventory.battery_model,
        "Battery Design Capacity": inventory.battery_design_capacity,
        "Battery Full Capacity": inventory.battery_full_capacity,
        "Battery Health %": inventory.battery_health,
        "Battery Cycle Count": inventory.battery_cycle_count,
        "Battery Status": inventory.battery_status,

        "Notes": inventory.notes,
    }


def load_existing_rows():

    if not CSV_FILE.exists():
        return []

    try:
        with open(CSV_FILE, newline="", encoding="utf-8") as f:

            reader = csv.DictReader(f)

            if reader.fieldnames != HEADERS:
                raise ValueError("Invalid CSV headers")

            return list(reader)

    except Exception:

        bad_file = CSV_FILE.with_suffix(".bad")

        try:
            if bad_file.exists():
                bad_file.unlink()

            CSV_FILE.rename(bad_file)

            print("WARNING: Invalid inventory CSV detected.")
            print("         Renamed to Inventory_Detail.bad")

        except Exception:
            pass

        return []


def write_inventory(inventory):

    rows = load_existing_rows()

    new_row = inventory_to_row(inventory)

    updated = False

    for i, row in enumerate(rows):

        if row.get("Serial Number") == inventory.serial:
            rows[i] = new_row
            updated = True
            break

    if not updated:
        rows.append(new_row)

    DATA_DIR.mkdir(exist_ok=True)

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(f, fieldnames=HEADERS)

        writer.writeheader()
        writer.writerows(rows)