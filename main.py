import platform
import subprocess

#!/usr/bin/env python3

from benchscan.benchscan import BenchScanner
from benchscan.version import VERSION, BUILD
from benchscan.health import check


LINE = "=" * 60


def main():

    check()
    scanner = BenchScanner()

    inventory = scanner.scan()

    print()
    print(LINE)
    print(f"                 BenchScan v{VERSION}")
    print(f"                  Build {BUILD}")
    print(LINE)
    print()

    print("System")
    print("-" * 60)
    print(f"Scan Date    : {inventory.scan_date}")
    print(f"Manufacturer : {inventory.manufacturer}")
    print(f"Model        : {inventory.model}")
    print(f"Serial       : {inventory.serial}")
    print()

    print("Processor")
    print("-" * 60)
    print(f"CPU          : {inventory.cpu}")
    print()

    print("Memory")
    print("-" * 60)
    print(f"Installed    : {inventory.ram_gb} GB")
    print()

    print("Storage")
    print("-" * 60)
    print(f"Capacity     : {inventory.storage_size}")
    print(f"Type         : {inventory.storage_type}")
    print(f"Model        : {inventory.storage_model}")
    print()

    print("Battery")
    print("-" * 60)

    if inventory.battery_present == "Yes":
        print("Present      : Yes")
        print(f"Manufacturer : {inventory.battery_manufacturer}")
        print(f"Model        : {inventory.battery_model}")
        print(f"Health       : {inventory.battery_health}%")
        print(f"Cycles       : {inventory.battery_cycle_count}")
        print(f"Status       : {inventory.battery_status}")
    else:
        print("Present      : No")

    print()
    print("-" * 60)

    inventory.notes = input("Notes (optional): ").strip()

    scanner.save(inventory)

    print()
    print("✓ Inventory_Detail.csv updated")
    print("✓ Inventory_Summary.csv updated")
    import subprocess

    print()
    print("=" * 60)
    print("Scan Complete.")
    print()

    input("Press ENTER to shut down...")

    print()
    print("BenchScan data saved to BENCHDATA USB partition.")
    print("System shutting down...")

    import time
    time.sleep(2)

    if platform.system() == "Linux":
        subprocess.run(["sudo", "poweroff"])
    else:
        print("Shutdown skipped (Windows test mode.")


if __name__ == "__main__":
    main()