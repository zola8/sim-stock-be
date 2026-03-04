import logging
from pathlib import Path


def get_file_path(filename: str) -> str:
    current_path = Path(__file__).resolve().parent
    target_path = Path(r"C:\DEV\sim-stock\sim-stock-be\src")

    if current_path == target_path:
        data_path = current_path / filename
        return str(data_path)
    else:
        logging.warning(f"current_path: {current_path}")
        data_path = current_path / "src" / filename
        return str(data_path)
