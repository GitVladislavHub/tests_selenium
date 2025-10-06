from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage
from config_reader import get_config

config = get_config()


class HomePage(BasePage):
    URL = config.BASE_STEAM
    SEARCH_LOCATOR = (By.XPATH, "//input[contains(@type, 'text') and contains(@role, 'combobox')]")
    SEARCH_BUTTON = (By.XPATH, "//form[contains(@role, 'search')]//button[contains(@type, 'submit')]")
    CAROUSEL_ITEMS = (By.XPATH,
                      "//div[contains(@class,'carousel_items') and "
                      "contains(@class,'store_capsule_container') and "
                      "contains(@class,'responsive_scroll_snap_ctn') and "
                      "contains(@class,'hero_row')]"
                      )

    def check_page(self):
        self.visible_unique_element(self.CAROUSEL_ITEMS)
        return self

    def input_game_name(self, game_name):
        element = self.wait.until(
            EC.visibility_of_element_located(self.SEARCH_LOCATOR))
        element.send_keys(game_name)
        return self

    def click_search_button(self, game_name):
        self.wait.until(EC.text_to_be_present_in_element_value(self.SEARCH_LOCATOR, game_name))
        button = self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON))
        button.click()
        return self
