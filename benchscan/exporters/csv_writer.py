import csv
import os


def write_inventory(inventory):

    filename = "data/Inventory_Detail.csv"

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as csvfile:

        writer = csv.writer(csvfile)

        if not file_exists:

            writer.writerow([
                "Scan Date",
                "Manufacturer",
                "Model",
                "Serial Number",
                "CPU",
                "RAM",
                "Storage Size",
                "Storage Type",
                "Storage Model"
            ])

        writer.writerow([
            inventory.scan_date,
            inventory.manufacturer,
            inventory.model,
            inventory.serial,
            inventory.cpu,
            f"{inventory.ram_gb} GB",
            inventory.storage_size,
            inventory.storage_type,
            inventory.storage_model
        ])