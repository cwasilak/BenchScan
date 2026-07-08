import re

from benchscan.utils.linux import run


def scan(inventory):

    total_ram = 0
    slots_used = 0
    slots_total = 0

    output = run("dmidecode -t memory")

    for line in output.splitlines():

        line = line.strip()

        if line.startswith("Memory Device"):
            slots_total += 1

        if line.startswith("Size:"):

            if "No Module Installed" in line:
                continue

            match = re.search(r"(\d+)\s+(MB|GB)", line)

            if match:

                amount = int(match.group(1))
                unit = match.group(2)

                if unit == "MB":
                    amount = amount / 1024

                total_ram += amount
                slots_used += 1

    inventory.ram_gb = int(round(total_ram))
    inventory.memory_slots = f"{slots_used}/{slots_total}"

    return inventory