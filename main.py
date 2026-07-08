#!/usr/bin/env python3

from benchscan.benchscan import BenchScanner


def main():

    scanner = BenchScanner()

    inventory = scanner.scan()

    print()
    print("BenchScan v1.0")
    print("=" * 50)

    print(f"Scan Date    : {inventory.scan_date}")
    print(f"Manufacturer : {inventory.manufacturer}")
    print(f"Model        : {inventory.model}")
    print(f"Serial       : {inventory.serial}")
    print()

    print(f"CPU          : {inventory.cpu}")
    print(f"RAM          : {inventory.ram_gb} GB")
    print()

    print(f"Storage      : {inventory.storage_size}")
    print(f"Type         : {inventory.storage_type}")
    print(f"Drive        : {inventory.storage_model}")

    print("=" * 50)
    print()


if __name__ == "__main__":
    main()