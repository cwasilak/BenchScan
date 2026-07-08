from dataclasses import dataclass
from datetime import datetime


@dataclass
class HardwareInventory:
    scan_date: str
    manufacturer: str = ""
    model: str = ""
    serial: str = ""
    cpu: str = ""
    ram_gb: int = 0
    memory_slots: str = ""
    storage_size: str = ""
    storage_type: str = ""
    storage_model: str = ""
    notes: str = ""


def new_inventory():
    return HardwareInventory(
        scan_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )