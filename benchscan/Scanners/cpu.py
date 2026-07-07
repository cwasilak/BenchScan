import subprocess


def get_cpu():
    try:
        cpu = subprocess.check_output(
            "lscpu | grep 'Model name'",
            shell=True,
            stderr=subprocess.DEVNULL,
            text=True
        )

        return cpu.split(":", 1)[1].strip()

    except Exception:
        return ""


def scan_cpu(inventory):
    inventory.cpu = get_cpu()
    return inventory