from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.chrome.options import Options
from enums import Language
from config_reader import ConfigReader


class Browser:
    _instance = None
    _driver = None
    _lang = None

    def __new__(cls, *args, **kwargs):

        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get(self, url: str, lang: Language = Language.RU):
        lang_value = lang.value
        if self._driver is None or self._lang != lang_value:
            self._create_driver(lang)
        self._driver.get(url)
        return self._driver

    def _create_driver(self, lang: str):
        if self._driver:
            try:
                self._driver.quit()
            except WebDriverException as e:
                (print(f"Ошибка при закрытии браузера! Возможно, он уже завершён {e}"))
            pass
        config = ConfigReader()
        options = Options()
        options.add_experimental_option("prefs", {"intl.accept_languages": str(lang)})

        window_size = config.browser.get("window_size", "1920,1080")
        options.add_argument(f"--window-size={window_size}")
        self._driver = webdriver.Chrome(options=options)
        self._lang = lang

    def quit(self):
        self._driver = None
        self._lang = None
        Browser._instance = None
