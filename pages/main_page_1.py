from elements.label import Label

from pages.base_page import BasePage


class MainLoginPage(BasePage):
    AUTH_LOC = "//div[contains(@class, 'example')]//p"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Authorization_page_1"
        self.text_element_loc = Label(browser, self.AUTH_LOC, description="Main_page -> Text")
        self.unique_element = self.text_element_loc

    def get_text_login(self):
        self.text_element_loc.wait_for_presence()
        text = self.text_element_loc.get_text()
        return text
