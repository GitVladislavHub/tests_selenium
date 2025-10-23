import random
from selenium.webdriver import ActionChains, Keys
from elements.web_element import WebElement
from pages.base_page import BasePage


class ActionsPage(BasePage):
    SLIDER_LOC = "//input[contains(@type, 'range')]"
    VALUE_SLIER_LOC = "//span[@id='range']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Actions_page"
        self.slider_element = WebElement(browser, self.SLIDER_LOC, description="action_element")
        self.value_slider_element = WebElement(browser, self.VALUE_SLIER_LOC, description="action_element")
        self.unique_element = self.slider_element

    def action_slider(self):
        slider_element = self.slider_element.wait_for_visible()
        current_value = float(self.value_slider_element.get_text())
        ActionChains(self.browser.driver).click(slider_element).perform()

        steps = random.randint(1, 10)

        for _ in range(steps):
            if current_value <= 0.5:
                key = Keys.ARROW_RIGHT
            elif current_value >= 4.5:
                key = Keys.ARROW_LEFT
            else:
                key = random.choice([Keys.ARROW_LEFT, Keys.ARROW_RIGHT])
            ActionChains(self.browser.driver).send_keys(key).perform()
            current_value = float(self.value_slider_element.get_text())
        return current_value

    def value_slider_final(self):
        current_value = float(self.value_slider_element.get_text())
        return current_value
