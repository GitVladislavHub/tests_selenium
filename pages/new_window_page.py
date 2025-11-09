from elements.label import Label
from pages.base_page import BasePage


class NewWindowPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div[contains(@class, 'example')]//h3"
    TEXT_ELEMENT_LOC = "//h3[contains(text(), 'New Window')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "New Window"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="New page -> Handlers page")
        self.text_element_loc = Label(browser, self.TEXT_ELEMENT_LOC, description="New page -> Text")

    def get_text_page(self):
        text = self.text_element_loc.get_text()
        return text
