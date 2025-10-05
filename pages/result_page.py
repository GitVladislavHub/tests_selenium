from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage, TIMEOUT_2


class ResultPage(BasePage):
    SORTED_BUTTON = By.XPATH, "//button[contains(@class, 'trigger') and contains(@id, 'sort_by_trigger')]"
    DECREASING_ELEMENT = By.XPATH, "//*[contains(@id, 'sort_by_droplist')]//a[contains(@id, 'Price_DESC')]"

    def success_open_page(self):
        return self.visible_unique_element(self.SORTED_BUTTON)

    def filter_button(self):
        self.click(self.SORTED_BUTTON)
        return self

    def decreasing_price(self):
        WebDriverWait(self.driver, TIMEOUT_2).until(EC.presence_of_element_located(self.DECREASING_ELEMENT))
        self.click(self.DECREASING_ELEMENT)
        return self
