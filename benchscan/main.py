#!/usr/bin/env python3

from benchscan.models import new_inventory
from benchscan.scanners.system import scan_system
from benchscan.scanners.cpu import scan_cpu
from benchscan.scanners.memory import scan_memory
from benchscan.scanners.storage import scan_storage


def run_scan():

    inventory = new_inventory()

    inventory = scan_system(inventory)
    inventory = scan_cpu(inventory)
    inventory = scan_memory(inventory)
    inventory = scan_storage(inventory)

    return inventory


if __name__ == "__main__":

    print()
    print("BenchScan v0.1")
    print("Starting hardware scan...")
    print()

    result = run_scan()

    result.display()