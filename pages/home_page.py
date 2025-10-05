from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage, TIMEOUT_2


class HomePage(BasePage):
    CAROUSEL_ITEMS = By.XPATH, (
        "//div[contains(@class,'carousel_items') and contains(@class,'store_capsule_container') "
        "and contains(@class,'responsive_scroll_snap_ctn') and contains(@class,'hero_row')]")

    def visible_el_home_page_steam(self):
        return self.visible_unique_element(self.CAROUSEL_ITEMS)

    def input_game_name(self, game_name):
        self.input_text_steam(self.SEARCH_LOCATOR, game_name)
        return self

    def click_button(self, game_name):
        WebDriverWait(self.driver, TIMEOUT_2).until(
            EC.text_to_be_present_in_element_value(self.SEARCH_LOCATOR, game_name))
        self.search_button(self.SEARCH_BUTTON)
        return self
