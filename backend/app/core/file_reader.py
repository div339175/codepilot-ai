from pathlib import Path


def read_file(file_path: Path) -> str:
    """
    Read a text file safely.
    Returns an empty string if the file cannot be read.
    """

    try:
        return file_path.read_text(
            encoding="utf-8",
            errors="ignore"
        )

    except Exception:
        return ""