from pathlib import Path

from benchscan.utils.linux import read_file


def _battery_path():
    power = Path("/sys/class/power_supply")

    if not power.exists():
        return None

    bats = sorted(power.glob("BAT*"))

    if not bats:
        return None

    return bats[0]


def _read(base, filename):
    if base is None:
        return ""

    return read_file(str(base / filename))


def _capacity(base):
    value = _read(base, "energy_full_design")
    if value:
        design = value
        full = _read(base, "energy_full")
    else:
        design = _read(base, "charge_full_design")
        full = _read(base, "charge_full")

    try:
        design = int(design)
        full = int(full)
        health = round((full / design) * 100, 1) if design > 0 else ""
    except Exception:
        design = ""
        full = ""
        health = ""

    return design, full, health


def scan(inventory):

    base = _battery_path()

    if base is None:
        inventory.battery_present = "No"
        return inventory

    inventory.battery_present = "Yes"

    inventory.battery_manufacturer = _read(base, "manufacturer")
    inventory.battery_model = _read(base, "model_name")

    design, full, health = _capacity(base)

    inventory.battery_design_capacity = design
    inventory.battery_full_capacity = full
    inventory.battery_health = health

    inventory.battery_cycle_count = _read(base, "cycle_count")
    inventory.battery_status = _read(base, "status")

    return inventory