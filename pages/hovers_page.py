from selenium.webdriver import ActionChains

from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class HoversPage(BasePage):
    HOVER_LOC_IMAGE_UNIQ = "//img[@alt='User Avatar']"

    HOVER_LOC_IMAGE = "(//img[@alt='User Avatar'])[{index}]"
    HOVER_HREF_LOC = "(//a[contains(text(), 'View profile')])[{index}]"
    TEXT_HOVER_LOC = "(//h5[contains(text(), 'name: user')])[{index}]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Hovers_page_1"
        self.hover_element_image_uniq = Label(browser, self.HOVER_LOC_IMAGE_UNIQ, description="Hover_image -> None")

        self.hover_element_image = Button(browser, self.HOVER_LOC_IMAGE, description="Hover_image_1 -> None")
        self.hover_element_href = Button(browser, self.HOVER_HREF_LOC,
                                         description="Hover_element_1 -> User_profile_page")

        self.unique_element = self.hover_element_image_uniq

    def get_text_hover_element(self, browser, user_index):
        image_locator = self.HOVER_LOC_IMAGE.format(index=user_index)
        image_element = Button(browser, image_locator, description="Hover_image -> None")

        hover_text_locator = self.TEXT_HOVER_LOC.format(index=user_index)
        text_hover_element = Label(browser, hover_text_locator, description="User_loc -> None")

        image_el = image_element.wait_for_visible()
        action_chains = ActionChains(browser.driver)
        action_chains.move_to_element(image_el).perform()

        text = text_hover_element.get_text()
        return text

    def click_view_profile(self, browser, user_index):
        href_locator = self.HOVER_HREF_LOC.format(index=user_index)
        hover_href_element = Button(browser, href_locator, description="Hover_href_1 -> User profile page")
        hover_href_element.click()
