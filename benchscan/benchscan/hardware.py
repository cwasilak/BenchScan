"""
BenchScan Hardware Detection
Version 0.1.0
"""

from models import HardwareInfo
from pathlib import Path
import subprocess
import re


def read_file(path, sudo=False):
    """Read a Linux file."""
    try:
        if sudo:
            result = subprocess.run(
                ["sudo", "cat", path],
                capture_output=True,
                text=True,
                check=True,
            )
            return result.stdout.strip()

        return Path(path).read_text().strip()

    except Exception:
        return ""


def run_command(command):
    """Run a shell command."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return ""


def get_hardware():

    info = HardwareInfo()

    info.scan_date = run_command("date '+%Y-%m-%d %H:%M:%S'")

    info.manufacturer = read_file("/sys/class/dmi/id/sys_vendor")

    info.model = read_file("/sys/class/dmi/id/product_name")

    info.serial = read_file(
        "/sys/class/dmi/id/product_serial",
        sudo=True
    )

    info.cpu = run_command("lscpu | grep 'Model name'")
    info.cpu = info.cpu.replace("Model name:", "").strip()

    # RAM
    ram = run_command("free -g | awk '/Mem:/ {print $2}'")
    info["ram_gb"] = ram + " GB"

    # Memory Slots
    sizes = run_command("sudo dmidecode -t memory | grep 'Size:'")

    used = 0
    total = 0

    for line in sizes.splitlines():
        if "No Module Installed" in line:
            total += 1
        elif "MB" in line or "GB" in line:
            used += 1
            total += 1

    info["memory_slots"] = f"{used}/{total}"

    # Storage
    storage = run_command("lsblk -dn -o NAME,SIZE,MODEL")

    info["storage_model"] = ""
    info["storage_size"] = ""
    info["storage_type"] = ""

    if storage:

        line = storage.splitlines()[0]
        parts = re.split(r"\s+", line, maxsplit=2)

        if len(parts) == 3:

            device = parts[0]
            size = parts[1]
            model = parts[2]

            info["storage_size"] = size
            info["storage_model"] = model

            bus = run_command(f"lsblk -dn -o TRAN /dev/{device}")

            if "nvme" in bus.lower():
                info["storage_type"] = "NVMe"
            elif "sata" in bus.lower():
                info["storage_type"] = "SSD/HDD"
            else:
                info["storage_type"] = bus

    return info