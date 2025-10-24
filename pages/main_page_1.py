from elements.label import Label
from logger.logger import Logger

from pages.base_page import BasePage


class MainLoginPage(BasePage):
    AUTH_LOC = "//div[contains(@class, 'example')]//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Authorization_page_1"
        self.loc_element = Label(browser, self.AUTH_LOC, description="Main_page -> Alert_Main_page -> Logging")

    def login(self):
        Logger.info("page opens...")
        self.loc_element.wait_for_presence()
        Logger.info("Successfully open page")
        text = self.loc_element.get_text()
        return text
