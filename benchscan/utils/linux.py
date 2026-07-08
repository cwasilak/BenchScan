import subprocess
from pathlib import Path


def run(command):
    """Run a shell command and return its output or an empty string."""
    try:
        result = subprocess.run(
            command,
            shell=True,
            capture_output=True,
            text=True,
            timeout=5
        )

        if result.returncode == 0:
            return result.stdout.strip()

    except Exception:
        pass

    return ""


def read_file(path):
    """Read a file and return its contents or an empty string."""
    try:
        return Path(path).read_text().strip()
    except Exception:
        return ""


def first_non_empty(*values):
    """Return the first non-empty value."""
    for value in values:
        if value and value.strip():
            return value.strip()
    return ""