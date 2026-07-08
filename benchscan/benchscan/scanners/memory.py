import subprocess
import re


def get_memory():
    try:
        output = subprocess.check_output(
            "dmidecode -t memory",
            shell=True,
            stderr=subprocess.DEVNULL,
            text=True
        )

        total = 0
        slots_used = 0
        slots_total = 0

        for line in output.splitlines():

            if "Memory Device" in line:
                slots_total += 1

            if "Size:" in line and "No Module Installed" not in line:
                size = re.search(r"(\d+)", line)
                if size:
                    total += int(size.group(1))

                    if int(size.group(1)) > 0:
                        slots_used += 1

        return total, slots_used, slots_total

    except Exception:
        return 0, 0, 0


def scan_memory(inventory):
    ram, used, total = get_memory()

    inventory.ram_gb = ram
    inventory.memory_configuration = f"{used}/{total}"

    return inventory