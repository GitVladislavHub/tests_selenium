import random
from selenium.webdriver import ActionChains, Keys
from elements.web_element import WebElement
from pages.base_page import BasePage


class ActionsPage(BasePage):
    SLIDER_LOC = "//input[contains(@type, 'range')]"
    VALUE_SLIDER_LOC = "//span[@id='range']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Actions_page"
        self.slider_element = WebElement(browser, self.SLIDER_LOC, description="ActionPage -> Click_slider_element")
        self.value_slider_element = WebElement(browser, self.VALUE_SLIDER_LOC,
                                               description="ActionPage -> Click_slider_element -> Text")
        self.unique_element = self.slider_element

    def action_slider(self, target_value):
        slider_element = self.slider_element.wait_for_visible()
        current_value = float(self.value_slider_element.get_text())
        ActionChains(self.browser.driver).click(slider_element).perform()

        while abs(current_value - target_value) > 0.1:
            if current_value < target_value:
                key = Keys.ARROW_RIGHT
            else:
                key = Keys.ARROW_LEFT

            ActionChains(self.browser.driver).send_keys(key).perform()
            current_value = float(self.value_slider_element.get_text())
        return current_value

    def final_value(self):
        current_value = float(self.value_slider_element.get_text())
        return current_value