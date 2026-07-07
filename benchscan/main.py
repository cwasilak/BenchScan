"""
BenchScan
Version 0.1
"""

from hardware import (
    get_manufacturer,
    get_model,
    get_serial,
)


def main():

    print("=" * 45)
    print("        BenchScan v0.1")
    print("=" * 45)

    print()

    print(f"Manufacturer : {get_manufacturer()}")
    print(f"Model        : {get_model()}")
    print(f"Serial       : {get_serial()}")

    print()


if __name__ == "__main__":
    main()
