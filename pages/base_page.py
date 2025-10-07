from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from config_reader import ConfigReader

config = ConfigReader()


class BasePage:
    def __init__(self, driver, timeout: int):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout or config.WAIT_DEFAULT)

    def open(self):
        self.driver.get(config.base_steam)

    def click(self, locator):
        el_cl = self.wait.until(EC.element_to_be_clickable(locator))
        el_cl.click()
