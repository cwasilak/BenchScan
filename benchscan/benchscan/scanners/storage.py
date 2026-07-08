import subprocess


def get_storage():

    try:
        drives = subprocess.check_output(
            "lsblk -d -o NAME,SIZE,ROTA,MODEL",
            shell=True,
            stderr=subprocess.DEVNULL,
            text=True
        )

        for line in drives.splitlines()[1:]:
            parts = line.split()

            if len(parts) >= 3:
                name = parts[0]
                size = parts[1]
                rota = parts[2]

                model = " ".join(parts[3:]) if len(parts) > 3 else ""

                if rota == "0":
                    storage_type = "SSD/NVMe"
                else:
                    storage_type = "HDD"

                return size, storage_type, model

    except Exception:
        pass

    return "", "", ""


def scan_storage(inventory):

    size, drive_type, model = get_storage()

    inventory.storage_size = size
    inventory.storage_type = drive_type
    inventory.storage_model = model

    return inventory