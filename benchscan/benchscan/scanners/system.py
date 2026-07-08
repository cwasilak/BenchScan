import subprocess


def get_command_output(command):
    try:
        result = subprocess.check_output(
            command,
            shell=True,
            stderr=subprocess.DEVNULL,
            text=True
        )
        return result.strip()
    except Exception:
        return ""


def get_manufacturer():
    return get_command_output(
        "dmidecode -s system-manufacturer"
    )


def get_model():
    return get_command_output(
        "dmidecode -s system-product-name"
    )


def get_serial():
    return get_command_output(
        "dmidecode -s system-serial-number"
    )


def scan_system(inventory):
    inventory.manufacturer = get_manufacturer()
    inventory.model = get_model()
    inventory.serial = get_serial()

    return inventory