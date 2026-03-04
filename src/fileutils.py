import logging
from pathlib import Path


def get_file_path(filename: str) -> str:
    current_path = Path(__file__).resolve().parent
    target_path = Path(r"C:\DEV\sim-stock\sim-stock-be\src")

    if current_path == target_path:
        data_path = current_path / filename
        logging.warning(f"data_path for file loading: {data_path}")
        return str(data_path)
    else:
        data_path = current_path / "src" / filename
        logging.warning(f"data_path for file loading: {data_path}")
        return str(data_path)
