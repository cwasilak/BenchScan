from benchscan.utils.linux import run


def scan(inventory):

    inventory.storage_size = "Unknown"
    inventory.storage_type = "Unknown"
    inventory.storage_model = "Unknown"

    output = run(
        "lsblk -d -b -o NAME,ROTA,TRAN,SIZE,MODEL | grep -v '^loop'"
    )

    for line in output.splitlines():

        parts = line.split(None, 4)

        if len(parts) < 5:
            continue

        name = parts[0]
        rota = parts[1]
        tran = parts[2]
        size = parts[3]
        model = parts[4].strip()

        # Skip USB drives (your BenchScan USB)
        if tran == "usb":
            continue

        try:
            size_gb = round(int(size) / (1024 ** 3))
            inventory.storage_size = f"{size_gb} GB"
        except Exception:
            pass

        inventory.storage_model = model

        if tran == "nvme":
            inventory.storage_type = "NVMe"

        elif rota == "0":
            inventory.storage_type = "SSD"

        else:
            inventory.storage_type = "HDD"

        break

    return inventory