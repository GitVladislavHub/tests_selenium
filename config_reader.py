import json
from functools import lru_cache
from pathlib import Path


class ConfigReader:
    CONFIG_PATH = Path(__file__).parent / "config.json"

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
    def WAIT_DEFAULT(self) -> int:
        return int(self.timeouts.get("wait_default", 10))

    @property
    def BASE_STEAM(self):
        return self.base_urls.get("steam", "https://store.steampowered.com/")


@lru_cache(maxsize=1)
def get_config() -> ConfigReader:
    """чтобы не читать файл каждый раз заново"""
    return ConfigReader()
