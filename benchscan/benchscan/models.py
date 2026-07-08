from dataclasses import dataclass, asdict
from datetime import datetime


@dataclass
class HardwareInventory:
    scan_date: str = ""
    manufacturer: str = ""
    model: str = ""
    serial: str = ""

    cpu: str = ""
    ram_gb: int = 0
    memory_configuration: str = ""

    storage_size: str = ""
    storage_type: str = ""
    storage_model: str = ""

    notes: str = ""

    def to_dict(self):
        return asdict(self)

    def display(self):
        print("=" * 50)
        print("BenchScan Hardware Inventory")
        print("=" * 50)

        for key, value in self.to_dict().items():
            print(f"{key}: {value}")

        print("=" * 50)


def new_inventory():
    return HardwareInventory(
        scan_date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )