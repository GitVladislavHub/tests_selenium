from selenium.webdriver.support.wait import WebDriverWait
from config_reader import ConfigReader
from conftest import driver

config = ConfigReader()


class BasePage:
    def __init__(self, driver, timeout):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout or config.timeouts["wait_default"])
        self.fast_wait = WebDriverWait(self.driver, config.timeouts["wait_default"], poll_frequency=0.1)
