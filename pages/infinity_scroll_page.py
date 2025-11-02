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


    #сырое решение, но, вроде работает
    def get_all_scroll_elements(self, age: int):
        lst_elements = []
        index = 1
        while len(lst_elements) < age:
            self.browser.scroll_js_down()
            current_loc = self.SCROLL_TEXT_LOC.format(index)
            element = Label(self.browser, current_loc)

            if element.wait_for_presence():
                lst_elements.append(element)
                index += 1
            else:
                element.wait_for_presence()
