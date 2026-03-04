import logging
from pathlib import Path


def get_file_path(filename: str) -> str:
    current_path = Path(__file__).resolve().parent

    if str(current_path).endswith('src'):
        data_path = current_path / filename
        logging.warning(f"data_path for file loading: {data_path}")
        return str(data_path)
    else:
        data_path = current_path / "src" / filename
        logging.warning(f"data_path for file loading: {data_path}")
        return str(data_path)
