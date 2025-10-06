from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from config_reader import get_config

config = get_config()


class BasePage:
    def __init__(self, driver, timeout: int):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout or config.WAIT_DEFAULT)

    def open(self, url):
        self.driver.get(url)
        return self

    def click(self, locator):
        el_cl = self.wait.until(EC.element_to_be_clickable(locator))
        el_cl.click()

    def visible_unique_element(self, locator) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
