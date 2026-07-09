# BenchScan

**BenchScan** is a portable hardware inventory appliance designed to quickly scan laptops from a bootable Linux USB. It automatically collects hardware information, maintains a detailed inventory, builds a summary report, and is optimized for processing large batches of systems.

Current Version: **v1.0.0**

---

# Features

* Automatic hardware detection
* Manufacturer
* Model
* Serial Number
* CPU
* Installed RAM
* Storage Capacity
* Storage Type (NVMe / SSD / HDD)
* Storage Model
* Battery Detection
* Battery Health
* Battery Cycle Count
* Battery Status
* Optional Technician Notes

---

# Reports

BenchScan generates two CSV files.

## Inventory_Detail.csv

Contains one record for every unique laptop scanned.

Duplicate scans of the same serial number update the existing record instead of creating duplicates.

## Inventory_Summary.csv

Groups identical systems together and displays:

* Quantity
* Manufacturer
* Model
* CPU
* RAM
* Storage Size
* Storage Type
* Battery Present
* Notes

---

# Logging

BenchScan automatically creates:

```
BenchScan.log
```

The log records:

* Scan Started
* Hardware Scan Completion
* Inventory Saved
* Summary Updated
* Scan Completed

This file is intended for troubleshooting and auditing.

---

# Project Structure

```
BenchScan/

├── benchscan/
│   ├── exporters/
│   ├── scanners/
│   ├── summary/
│   ├── models.py
│   ├── paths.py
│   ├── version.py
│   ├── logger.py
│   ├── health.py
│   └── benchscan.py
│
├── data/
│   ├── Inventory_Detail.csv
│   ├── Inventory_Summary.csv
│   └── BenchScan.log
│
├── main.py
└── README.md
```

---

# Requirements

* Python 3
* Linux (Debian recommended)
* Root access when required for hardware detection

---

# Running BenchScan

```
python3 main.py
```

or

```
sudo python3 main.py
```

depending on your Linux environment.

---

# Planned USB Appliance

BenchScan is intended to run from a dedicated bootable USB.

Startup workflow:

1. Boot laptop from USB
2. BenchScan starts automatically
3. Hardware is scanned
4. Optional notes entered
5. CSV reports updated
6. Press ENTER to shut down
7. Move USB to the next laptop

No Linux knowledge is required during normal operation.

---

# Export Location

BenchScan automatically detects the best export location.

Priority order:

1. `/media/user/BENCHSCAN_DATA`
2. `/mnt/BENCHSCAN_DATA`
3. Local `data` folder

This allows the same software to run both during development and on the production USB appliance.

---

# Versioning

BenchScan follows Semantic Versioning.

Examples:

* v1.0.0 – Initial release
* v1.0.1 – Bug fixes
* v1.1.0 – New features
* v2.0.0 – Major release

---

# Development Goals

Version 1.0 focuses on:

* Stability
* Accurate hardware inventory
* Reliable CSV reporting
* Duplicate protection
* Simple technician workflow

Future releases may include:

* SMART drive health
* BIOS information
* TPM detection
* Network adapter inventory
* Additional hardware diagnostics

---

# License

This project is provided as-is without warranty.

---

# Author

Developed by Craig Wasilak.
