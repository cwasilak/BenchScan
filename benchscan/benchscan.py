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

        scan_system(inventory)
        scan_cpu(inventory)
        scan_memory(inventory)
        scan_storage(inventory)
        scan_battery(inventory)

        print(vars(inventory))

        write_inventory(inventory)

        build_summary()

        return inventory