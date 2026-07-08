from pathlib import Path


def _read(path):
    try:
        return Path(path).read_text().strip()
    except Exception:
        return ""


def scan(inventory):
    inventory.manufacturer = _read("/sys/class/dmi/id/sys_vendor")
    inventory.model = _read("/sys/class/dmi/id/product_name")
    inventory.serial = _read("/sys/class/dmi/id/product_serial")

    return inventory