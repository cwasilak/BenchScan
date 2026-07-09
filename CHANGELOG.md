# Changelog

All notable changes to BenchScan will be documented in this file.

The project follows Semantic Versioning (SemVer).

---

## [1.0.0] - 2026-07-09

### Initial Release

#### Added

* Hardware inventory scanner
* System manufacturer detection
* Model detection
* Serial number detection
* CPU detection
* Installed RAM detection
* Storage size detection
* Storage type detection (NVMe / SSD / HDD)
* Storage model detection
* Battery detection
* Battery manufacturer detection
* Battery model detection
* Battery design capacity detection
* Battery full capacity detection
* Battery health calculation
* Battery cycle count detection
* Battery charging status detection
* Optional technician notes
* Automatic duplicate detection using serial number
* Detailed inventory CSV export
* Summary inventory CSV export
* Automatic summary generation
* Automatic export location detection
* CSV corruption recovery
* Scan progress indicators
* Startup environment health check
* Scan logging
* Version and build information
* Centralized path management

#### Changed

* Project reorganized into modular scanners and exporters.
* Export paths centralized for easier maintenance.
* Summary report groups identical systems by hardware configuration.

#### Fixed

* Prevented duplicate inventory entries.
* Automatic recovery from invalid or corrupted inventory CSV files.
* Improved reliability of report generation.

---

## Future Releases

### Planned for 1.1.0

* Faster boot appliance
* Automatic startup after boot
* Windows-readable export partition
* Additional hardware diagnostics
* User interface improvements
* Performance optimizations

---

## Version History

| Version | Date       | Notes                  |
| ------: | ---------- | ---------------------- |
|   1.0.0 | 2026-07-09 | Initial public release |
