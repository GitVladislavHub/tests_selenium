from elements.label import Label
from elements.multi_web_element import MultiWebElement
from pages.base_page import BasePage


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div//h3[contains(text(), 'Infinite Scroll')]"
    SCROLL_TEXT_LOC = "//div[contains(@class, 'jscroll-added')][{}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Infinity Scroll Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="Unique_element page -> None")

        self.elements_text_loc = Label(browser, self.SCROLL_TEXT_LOC, description="Elements_text_loc -> None")

        self.elements_text_loc_all = MultiWebElement(browser, self.SCROLL_TEXT_LOC,
                                                     description="Elements_text_loc -> None")

    def get_element_by_index(self, index: int) -> Label:
        return Label(self.browser, self.SCROLL_TEXT_LOC.format(index))
