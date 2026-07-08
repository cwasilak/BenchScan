from benchscan.models import new_inventory
from benchscan.scanners.system import scan


def main():
    inventory = new_inventory()
    scan(inventory)

    print("\nBenchScan v1.0")
    print("=" * 50)
    print(f"Scan Date    : {inventory.scan_date}")
    print(f"Manufacturer : {inventory.manufacturer or 'Unknown'}")
    print(f"Model        : {inventory.model or 'Unknown'}")
    print(f"Serial       : {inventory.serial or 'Unknown'}")
    print("=" * 50)


if __name__ == "__main__":
    main()