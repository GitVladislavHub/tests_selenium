from selenium.webdriver.support.wait import WebDriverWait
from config_reader import ConfigReader
from conftest import driver

config = ConfigReader()


class BasePage:
    url = config.base_steam

    def __init__(self, driver, timeout: int):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout or config.WAIT_DEFAULT)
