from elements.button import Button
from pages.base_page import BasePage


class HoversPage(BasePage):
    HOVER_LOC = ""
    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Hovers_page_1"
        self.hover_element = Button(browser, self., description="Hovers_loc_1")
        self.unique_element = self.hover_element

    def click_hover(self):
        pass
