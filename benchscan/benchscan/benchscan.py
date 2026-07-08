from hardware import get_hardware

info = get_hardware()

print("=" * 60)
print("                 BENCHSCAN v0.1")
print("=" * 60)

print()

print(f"Scan Date    : {info['scan_date']}")
print()
print(f"Manufacturer : {info['manufacturer']}")
print(f"Model        : {info['model']}")
print(f"Serial       : {info['serial']}")
print(f"Asset Tag    : {info['asset_tag']}")
print()
print(f"CPU          : {info['cpu']}")
print(f"RAM          : {info['ram_gb']}")
print(f"Memory Slots : {info['memory_slots']}")
print()
print(f"Storage Model: {info['storage_model']}")
print(f"Storage Size : {info['storage_size']}")
print(f"Storage Type : {info['storage_type']}")
print()

input("Notes (optional): ")