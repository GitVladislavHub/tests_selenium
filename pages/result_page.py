from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ResultPage(BasePage):
    FILTER_BUTTON = (By.XPATH, "//button[contains(@class, 'trigger') and contains(@id, 'sort_by_trigger')]")
    DECREASING_ELEMENT = (By.XPATH, "//*[contains(@id, 'sort_by_droplist')]//a[contains(@id, 'Price_DESC')]")

    def wait_success_open_page(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.FILTER_BUTTON))
            return True
        except TimeoutException:
            return False

    def filter_button(self):
        self.click(self.FILTER_BUTTON)

    def reduce_the_price(self):
        self.wait.until(EC.element_to_be_clickable(self.DECREASING_ELEMENT))
        self.click(self.DECREASING_ELEMENT)
