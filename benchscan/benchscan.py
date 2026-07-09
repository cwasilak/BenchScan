from benchscan.models import new_inventory

from benchscan.scanners.system import scan as scan_system
from benchscan.scanners.cpu import scan as scan_cpu
from benchscan.scanners.memory import scan as scan_memory
from benchscan.scanners.storage import scan as scan_storage
from benchscan.scanners.battery import scan as scan_battery

from benchscan.exporters.csv_writer import write_inventory
from benchscan.summary.summary import build_summary
from benchscan.logger import log


class BenchScanner:

    def scan(self):

        inventory = new_inventory()

        log("Scan Started")

        print("Scanning Hardware...")
        print()

        scan_system(inventory)
        print("✓ System")
        log("System Scan Complete")

        scan_cpu(inventory)
        print("✓ CPU")
        log("CPU Scan Complete")

        scan_memory(inventory)
        print("✓ Memory")
        log("Memory Scan Complete")

        scan_storage(inventory)
        print("✓ Storage")
        log("Storage Scan Complete")

        scan_battery(inventory)
        print("✓ Battery")
        log("Battery Scan Complete")

        print()

        return inventory

    def save(self, inventory):

        print("Generating Reports...")
        print()

        log(f"Saving {inventory.manufacturer} {inventory.model}")
        log(f"Serial: {inventory.serial}")

        write_inventory(inventory)
        print("✓ Inventory")
        log("Inventory Updated")

        build_summary()
        print("✓ Summary")
        log("Summary Updated")

        log("Scan Complete")