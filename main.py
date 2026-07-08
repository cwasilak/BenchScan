from benchscan.models import new_inventory
from benchscan.scanners.system import scan
from benchscan.scanners.cpu import scan as scan_cpu
from benchscan.scanners.memory import scan as scan_memory


def main():
    inventory = new_inventory()
    scan(inventory)
    scan_cpu(inventory)
    scan_memory(inventory)


    print("\nBenchScan v1.0")
    print("=" * 50)
    print(f"Scan Date    : {inventory.scan_date}")
    print(f"Manufacturer : {inventory.manufacturer or 'Unknown'}")
    print(f"Model        : {inventory.model or 'Unknown'}")
    print(f"Serial       : {inventory.serial or 'Unknown'}")
    print(f"CPU          : {inventory.cpu or 'Unknown'}")
    print(f"RAM          : {inventory.ram_gb} GB")
    print(f"Slots        : {inventory.memory_slots}")
    print("=" * 50)


if __name__ == "__main__":
    main()