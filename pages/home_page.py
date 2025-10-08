from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from config_reader import ConfigReader
from pages.base_page import BasePage

config = ConfigReader()


class HomePage(BasePage):
    URL = config.base_steam
    SEARCH_LOCATOR = (By.XPATH, "//input[contains(@type, 'text') and contains(@role, 'combobox')]")
    SEARCH_BUTTON = (By.XPATH, "//form[contains(@role, 'search')]//button[contains(@type, 'submit')]")

    def is_check_page(self) -> bool:
        try:
            self.wait.until(EC.visibility_of_element_located(self.SEARCH_BUTTON))
            return True
        except TimeoutException:
            return False

    def input_game_name(self, game_name):
        element = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_LOCATOR))
        element.send_keys(game_name)
        return self

    def search_game(self, game_name):
        self.wait.until(EC.text_to_be_present_in_element_value(self.SEARCH_LOCATOR, game_name))
        button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        button.click()
        return self
