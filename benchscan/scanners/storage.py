import json

from benchscan.utils.linux import run


def scan(inventory):

    inventory.storage_size = "Unknown"
    inventory.storage_type = "Unknown"
    inventory.storage_model = "Unknown"

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

            inventory.storage_size = f"{round(size / (1024**3))} GB"
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