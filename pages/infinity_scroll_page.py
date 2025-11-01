from elements.label import Label
from elements.multi_web_element import MultiWebElement
from elements.web_element import WebElement
from pages.base_page import BasePage


class InfinityScrollPage(BasePage):
    UNIQUE_ELEMENT_LOC = "//div//h3[contains(text(), 'Infinite Scroll')]"
    SCROLL_TEXT_LOC = "//div[contains(@class, 'jscroll-added')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Infinity Scroll Page"
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="Unique_element page -> None")

        self.elements_text_loc = Label(browser, self.SCROLL_TEXT_LOC, description="Elements_text_loc -> None")

        self.elements_text_loc_all = MultiWebElement(browser, self.SCROLL_TEXT_LOC, description="Elements_text_loc -> None")

    def get_all_scroll_elements(self, age=24):
        lst_elements = []
        while len(lst_elements) < 24:
            self.browser.scroll_js_down()
            if self.elements_text_loc.wait_for_visible():
                lst_elements.append(self.elements_text_loc)
