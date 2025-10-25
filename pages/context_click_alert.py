from selenium.webdriver import ActionChains

from elements.button import Button
from pages.base_page import BasePage


class ContextClickAlert(BasePage):
    CONTEXT_PAGE_LOC = "//div[contains(@id, 'hot-spot')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "context_click_alert_page"
        self.element_context_menu = Button(browser, self.CONTEXT_PAGE_LOC, description="AlertPage -> Click -> Alert_element")
        self.unique_element = self.element_context_menu

    def right_click_context_menu(self):
        right_click_element = self.element_context_menu.wait_for_visible()
        action_chains = ActionChains(self.browser.driver)
        action_chains.context_click(right_click_element).perform()

        self.browser.wait_alert_present()
        alert_text = self.browser.get_alert_text()
        return alert_text
