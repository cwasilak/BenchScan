"""
Battery Scanner
"""

from pathlib import Path


class BatteryScanner:
    """Reads battery information from Linux sysfs."""

    def __init__(self):
        self.base = None

        power = Path("/sys/class/power_supply")

        if power.exists():
            bats = sorted(power.glob("BAT*"))
            if bats:
                self.base = bats[0]

    def _read(self, filename):
        if self.base is None:
            return ""

        path = self.base / filename

        try:
            return path.read_text().strip()
        except Exception:
            return ""

    def _capacity(self, primary, alternate):
        value = self._read(primary)

        if value == "":
            value = self._read(alternate)

        try:
            return int(value)
        except Exception:
            return None

    def scan(self):
        """
        Returns battery information.
        """

        if self.base is None:
            return {
                "Battery Present": "No",
                "Battery Manufacturer": "",
                "Battery Model": "",
                "Battery Design Capacity": "",
                "Battery Full Capacity": "",
                "Battery Health %": "",
                "Battery Cycle Count": "",
                "Battery Status": ""
            }

        design = self._capacity(
            "energy_full_design",
            "charge_full_design"
        )

        full = self._capacity(
            "energy_full",
            "charge_full"
        )

        health = ""

        if design and full and design > 0:
            health = round((full / design) * 100, 1)

        return {
            "Battery Present": "Yes",
            "Battery Manufacturer": self._read("manufacturer"),
            "Battery Model": self._read("model_name"),
            "Battery Design Capacity": design if design else "",
            "Battery Full Capacity": full if full else "",
            "Battery Health %": health,
            "Battery Cycle Count": self._read("cycle_count"),
            "Battery Status": self._read("status")
        }