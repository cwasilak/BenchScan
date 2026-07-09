from benchscan.models import new_inventory

from benchscan.scanners.system import scan as scan_system
from benchscan.scanners.cpu import scan as scan_cpu
from benchscan.scanners.memory import scan as scan_memory
from benchscan.scanners.storage import scan as scan_storage
from benchscan.scanners.battery import scan as scan_battery

from benchscan.exporters.csv_writer import write_inventory
from benchscan.summary.summary import build_summary


class BenchScanner:

    def scan(self):

        inventory = new_inventory()

        print("Scanning Hardware...")
        print()

        scan_system(inventory)
        print("✓ System")

        scan_cpu(inventory)
        print("✓ CPU")

        scan_memory(inventory)
        print("✓ Memory")

        scan_storage(inventory)
        print("✓ Storage")

        scan_battery(inventory)
        print("✓ Battery")

        print()

        return inventory

    def save(self, inventory):

        print("Generating Reports...")
        print()

        write_inventory(inventory)
        print("✓ Inventory")

        build_summary()
        print("✓ Summary")