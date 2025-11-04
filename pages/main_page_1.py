from elements.label import Label

from pages.base_page import BasePage


class MainLoginPage(BasePage):
    AUTH_LOC = "//div[contains(@class, 'example')]//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Authorization_page_1"
        self.loc_element = Label(browser, self.AUTH_LOC, description="Main_page -> Alert_Main_page -> Logging")
        self.unique_element = self.loc_element

    def get_text_login(self):
        self.loc_element.wait_for_presence()
        text = self.loc_element.get_text()
        return text
