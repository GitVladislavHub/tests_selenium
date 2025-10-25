import json
from pathlib import Path


class ConfigReader:
    _instance = None
    CONFIG_PATH = Path(__file__).parent / "config.json"

    def __init__(self, path: Path = CONFIG_PATH):
        with open(path, "r", encoding="utf-8") as f:
            self._data = json.load(f)

    @property
    def base_urls(self):
        return self._data["base_urls"]

    @property
    def pc_window_size(self):
        return self._data["pc_window_size"]