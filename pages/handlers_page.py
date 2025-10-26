from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class HandlersPage(BasePage):
    HREF_HANDLER_LOC = "//a[contains(text(), 'Click Here')]"
    TEXT_HANDLER_LOC = "//h3[contains(text(), 'New Window')]"
    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "handlers_page"
        self.click_window_href_button = Button(browser, self.HREF_HANDLER_LOC, description="Handlers Page -> New Window")
        self.unique_element = self.click_window_href_button
        self.text_handler = Label(browser, self.TEXT_HANDLER_LOC, description="Text_on_new_page -> None")

    def click_href_button_handler(self):
        self.click_window_href_button.wait_for_clickable()
        self.click_window_href_button.click()

        self.browser.switch_to_window("New Window")

        self.text_handler.wait_for_visible()
        text = self.text_handler.get_text()
        return text

    def back_on_page(self):
        self.browser.switch_to_default_window()
        self.click_window_href_button.wait_for_visible()
        text_main_page = self.click_window_href_button.get_text()
        return text_main_page

    def close_pages(self):
       self.browser.close_tab_by_index(2)
       self.browser.close_tab_by_index(1)






