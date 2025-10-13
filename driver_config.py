from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config_reader import ConfigReader


class DriverConfig:
    def __init__(self):
        self.config = ConfigReader()

    def create_driver(self):
        options = Options()
        driver = webdriver.Chrome(options=options)
        driver.set_window_size(1920, 1080)
        driver.implicitly_wait(self.config.timeouts["wait_default"])
        return driver
