from benchscan.models import new_inventory
from benchscan.scanners.system import scan


def main():
    inventory = new_inventory()

    scan(inventory)

    print("BenchScan")
    print("-" * 40)
    print(f"Scan Date    : {inventory.scan_date}")
    print(f"Manufacturer : {inventory.manufacturer}")
    print(f"Model        : {inventory.model}")
    print(f"Serial       : {inventory.serial}")


if __name__ == "__main__":
    main()