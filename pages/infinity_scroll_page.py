from elements.label import Label
from pages.base_page import BasePage


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div//h3[contains(text(), 'Infinite Scroll')]"
    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Infinity Scroll Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="Unique_element page -> None")

    def scroll_down(self):
        pass