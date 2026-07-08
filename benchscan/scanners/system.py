from benchscan.utils.linux import read_file, run, first_non_empty


def scan(inventory):

    inventory.manufacturer = first_non_empty(
        read_file("/sys/class/dmi/id/sys_vendor"),
        run("dmidecode -s system-manufacturer")
    )

    inventory.model = first_non_empty(
        read_file("/sys/class/dmi/id/product_name"),
        run("dmidecode -s system-product-name")
    )

    inventory.serial = first_non_empty(
        read_file("/sys/class/dmi/id/product_serial"),
        run("dmidecode -s system-serial-number")
    )

    return inventory