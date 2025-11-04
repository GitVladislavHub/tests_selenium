from elements.label import Label
from pages.base_page import BasePage


class ViewProfilePage(BasePage):
    USER_PAGE_TEXT_LOC = "//h2[contains(text(), 'Sinatra')]"
    UNIQUE_ELEMENT_LOC = "//h2[contains(text(), 'Sinatra')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = 'View Profile Page'
        self.unique_element = Label(browser, self.UNIQUE_ELEMENT_LOC, description="View Profile Page -> Text")
        self.profile_loc = Label(browser, self.USER_PAGE_TEXT_LOC, description="View Profile Page -> Text")

    def get_text_view_profile(self):
        text = self.profile_loc.get_text()
        return text
