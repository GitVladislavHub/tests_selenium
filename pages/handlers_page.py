from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class HandlersPage(BasePage):
    HREF_HANDLER_LOC = "//a[contains(text(), 'Click Here')]"
    TEXT_ELEMENT_LOC = "//div[contains(@class, 'example')]//h3"
    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "handlers_page"
        self.click_window_href_button = Button(browser, self.HREF_HANDLER_LOC,
                                               description="Handlers Page -> New Window")
        self.text_element_loc = Label(browser, self.TEXT_ELEMENT_LOC,
                                               description="Handlers Page -> New Window")

        self.unique_element = self.click_window_href_button

    def click_href_button_handler(self):
        self.click_window_href_button.click()


    def get_text_element(self):
        text = self.text_element_loc.get_text()
        return text
