import json
from pathlib import Path


class ConfigReader:
    _instance = None
    CONFIG_PATH = Path(__file__).parent / "config.json"
    WAIT_DEFAULT = 10

    def __init__(self, path: Path = CONFIG_PATH):
        with open(path, "r", encoding="utf-8") as f:
            self._data = json.load(f)

    @property
    def base_urls(self) -> dict:
        return self._data.get("base_urls", {})

    @property
    def timeouts(self) -> dict:
        return self._data.get("timeouts", {})

    @property
    def browser(self) -> dict:
        return self._data.get("browser", {})

    @property
    def base_steam(self):
        return self.base_urls.get("steam", "https://store.steampowered.com/")

