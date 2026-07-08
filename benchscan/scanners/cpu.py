from benchscan.utils.linux import run, first_non_empty


def scan(inventory):

    cpu = first_non_empty(
        run("lscpu | grep 'Model name' | cut -d':' -f2"),
        run("cat /proc/cpuinfo | grep 'model name' | head -1 | cut -d':' -f2")
    )

    inventory.cpu = cpu.strip()

    return inventory