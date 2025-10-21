from elements.label import Label
from logger.logger import Logger

from pages.base_page import BasePage


class MainLoginPage(BasePage):
    AUTH_LOC = "//div[contains(@class, 'example')]//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Authorization_page_1"
        self.loc_element = Label(browser, self.AUTH_LOC, description="authorization page")

    def login(self):
        Logger.info("Logging in...")
        self.loc_element.wait_for_visible()
        Logger.info("Successfully logged in")
        text = self.loc_element.get_text()
        return text
