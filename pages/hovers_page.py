from selenium.webdriver import ActionChains
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage


class HoversPage(BasePage):
    HOVER_LOC_IMAGE = "(//img[@alt='User Avatar'])[1]"
    HOVER_HREF_LOC = "(//a[contains(text(), 'View profile')])[1]"
    TEXT_HOVER_LOC = "//h5[contains(text(), 'name: user1')]"

    HOVER_LOC_IMAGE_2 = "(//img[@alt='User Avatar'])[2]"
    HOVER_HREF_LOC_2 = "(//a[contains(text(), 'View profile')])[2]"
    TEXT_HOVER_LOC_2 = "//h5[contains(text(), 'name: user2')]"

    HOVER_LOC_IMAGE_3 = "(//img[@alt='User Avatar'])[3]"
    HOVER_HREF_LOC_3 = "(//a[contains(text(), 'View profile')])[3]"
    TEXT_HOVER_LOC_3 = "//h5[contains(text(), 'name: user3')]"

    USER_PAGE_TEXT_LOC = "//h2[contains(text(), 'Sinatra')]"

    def __init__(self, browser):
        super().__init__(browser)

        self.page_name = "Hovers_page_1"
        self.hover_element_image_1 = Button(browser, self.HOVER_LOC_IMAGE, description="Hover_image_1 -> None")
        self.hover_element_href_1 = Button(browser, self.HOVER_HREF_LOC,
                                           description="Hover_element_1 -> User_profile_page")
        self.text_hover_element_1 = Label(browser, self.TEXT_HOVER_LOC, description="User_loc -> None")


        self.hover_element_image_2 = Button(browser, self.HOVER_LOC_IMAGE_2, description="Hover_image_1 -> None")
        self.hover_element_href_2 = Button(browser, self.HOVER_HREF_LOC_2,
                                           description="Hover_element_1 -> User_profile_page")
        self.text_hover_element_2 = Label(browser, self.TEXT_HOVER_LOC_2, description="User_loc -> None")


        self.hover_element_image_3 = Button(browser, self.HOVER_LOC_IMAGE_3, description="Hover_image_1 -> None")
        self.hover_element_href_3 = Button(browser, self.HOVER_HREF_LOC_3,
                                           description="Hover_element_1 -> User_profile_page")
        self.text_hover_element_3 = Label(browser, self.TEXT_HOVER_LOC_3, description="User_loc -> None")


        self.user_element_loc = Label(browser, self.USER_PAGE_TEXT_LOC, description="User_loc -> None")

        self.unique_element = self.hover_element_image_1

    def click_hover_user_1(self):
        hover_element_mouse = self.hover_element_image_1.wait_for_visible()
        action_chains = ActionChains(self.browser.driver)
        action_chains.move_to_element(hover_element_mouse).perform()
        self.text_hover_element_1.wait_for_visible()
        text_1 = self.text_hover_element_1.get_text()
        return text_1

    def click_href_hover_user_1(self):
        action_chains = ActionChains(self.browser.driver)
        link_element = self.hover_element_href_1.wait_for_clickable()
        action_chains.click(link_element).perform()
        self.user_element_loc.wait_for_visible()
        url = self.browser.driver.current_url
        return url

    def go_on_hovers_page(self):
        self.browser.go_back()
        return self.hover_element_image_1.wait_for_visible()

    def click_hover_user_2(self):
        hover_element_mouse = self.hover_element_image_2.wait_for_visible()
        action_chains = ActionChains(self.browser.driver)
        action_chains.move_to_element(hover_element_mouse).perform()
        self.text_hover_element_2.wait_for_visible()
        text_1 = self.text_hover_element_2.get_text()
        return text_1

    def click_href_hover_user_2(self):
        action_chains = ActionChains(self.browser.driver)
        link_element = self.hover_element_href_2.wait_for_clickable()
        action_chains.click(link_element).perform()
        self.user_element_loc.wait_for_visible()
        url = self.browser.driver.current_url
        return url

    def click_hover_user_3(self):
        hover_element_mouse = self.hover_element_image_3.wait_for_visible()
        action_chains = ActionChains(self.browser.driver)
        action_chains.move_to_element(hover_element_mouse).perform()
        self.text_hover_element_3.wait_for_visible()
        text_1 = self.text_hover_element_3.get_text()
        return text_1

    def click_href_hover_user_3(self):
        action_chains = ActionChains(self.browser.driver)
        link_element = self.hover_element_href_3.wait_for_clickable()
        action_chains.click(link_element).perform()
        self.user_element_loc.wait_for_visible()
        url = self.browser.driver.current_url
        return url
