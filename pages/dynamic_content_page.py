import time

from selenium.webdriver.common.by import By

from config_reader import ConfigReader
from elements.label import Label
from elements.multi_web_element import MultiWebElement
from pages.base_page import BasePage
from elements.base_element import BaseElement

config = ConfigReader()


class DynamicContentPage(BasePage):
    REFRESH_IMAGE_LOC = "//img[contains(@src, 'avatars')]"
    DYNAMIC_CONTENT_LOC_2 = "(//div[contains(@class, 'large-2 columns')])[1]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "dynamic_content_page"
        self.dynamic_content_loc_2 = Label(browser, self.DYNAMIC_CONTENT_LOC_2, description="All page images")
        self.unique_element = self.dynamic_content_loc_2

    def refreshing_page_dynamic_content(self):
        while True:
            images_lst = self.browser.driver.find_elements(By.XPATH, self.REFRESH_IMAGE_LOC)
            print(f"Найдено изображений: {len(images_lst)}")

            for idx, img in enumerate(images_lst):
                src = img.get_attribute("src")
                filename = src.split("/")[-1]
                print(f"  {idx}: {filename}")

            for i in range(len(images_lst)):
                for j in range(i + 1, len(images_lst)):
                    src_i = images_lst[i].get_attribute("src").split("/")[-1]
                    src_j = images_lst[j].get_attribute("src").split("/")[-1]
                    print(f"Сравниваю: {src_i} vs {src_j}")
                    if src_i == src_j:
                        return

            self.browser.refresh_page()
            self.unique_element.wait_for_visible()
