from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from enums import Language


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
            self._create_driver(lang_value)
        self._driver.get(url)
        return self._driver

    def _create_driver(self, lang: str):
        if self._driver:
            try:
                self._driver.quit()
            except Exception:
                pass
        options = Options()
        options.add_argument("window-size=1920,1080")
        options.add_experimental_option("prefs", {"intl.accept_languages": lang})
        self._driver = webdriver.Chrome(options=options)
        self._lang = lang

    def quit(self):
        if self._driver:
            try:
                self._driver.quit()
            except Exception:
                pass
        self._driver = None
        self._lang = None
        Browser._instance = None
