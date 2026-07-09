from datetime import datetime

from benchscan.paths import DATA_DIR

LOG_FILE = DATA_DIR / "BenchScan.log"


def log(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"{timestamp}  {message}\n")