import json

from benchscan.utils.linux import run


def scan(inventory):

    inventory.storage_size = "Unknown"
    inventory.storage_type = "Unknown"
    inventory.storage_model = "Unknown"

def format_storage_size(size_bytes):
    """
    Return common marketed drive sizes instead of binary GiB.
    """
    gb = size_bytes / 1_000_000_000

    common_sizes = [
        32, 64, 128, 160, 180,
        240, 250, 256,
        480, 500, 512,
        960, 1000, 1024,
        2000, 2048,
        4000, 4096,
        8000
    ]

    closest = min(common_sizes, key=lambda x: abs(x - gb))

    if closest >= 1000:
        if closest in (1000, 2000, 4000, 8000):
            return f"{closest // 1000} TB"
        else:
            return f"{closest / 1024:.0f} TB"

    return f"{closest} GB"

    output = run("lsblk -J -d -b -o NAME,ROTA,TRAN,SIZE,MODEL,TYPE")

    if not output:
        return inventory

    try:
        data = json.loads(output)

        for drive in data["blockdevices"]:

            # Skip loop devices
            if drive.get("type") != "disk":
                continue

            # Skip the USB boot drive
            if drive.get("tran") == "usb":
                continue

            size = int(drive.get("size", 0))

            inventory.storage_size = format_storage_size(size)
            inventory.storage_model = (drive.get("model") or "").strip()

            tran = drive.get("tran")
            rota = drive.get("rota")

            if tran == "nvme":
                inventory.storage_type = "NVMe"

            elif rota:
                inventory.storage_type = "HDD"

            else:
                inventory.storage_type = "SSD"

            break

    except Exception:
        pass

    return inventory