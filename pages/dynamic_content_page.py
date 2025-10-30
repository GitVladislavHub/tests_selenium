from config_reader import ConfigReader
from elements.label import Label
from elements.multi_web_element import MultiWebElement
from logger.logger import Logger
from pages.base_page import BasePage

config = ConfigReader()


class DynamicContentPage(BasePage):
    REFRESH_IMAGE_LOC = "(//img[contains(@src, 'avatars')])[{}]"
    DYNAMIC_CONTENT_LOC_2 = "(//div[contains(@class, 'large-2 columns')])[1]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "dynamic_content_page"
        self.dynamic_content_loc_2 = Label(browser, self.DYNAMIC_CONTENT_LOC_2, description="All page images")
        self.images_multi = MultiWebElement(browser, self.REFRESH_IMAGE_LOC, description="Dynamic images")
        self.unique_element = self.dynamic_content_loc_2

    def get_lst_elements_on_content_page(self):
        images_list = []
        all_images = self.images_multi
        for image_element in all_images:
            src = image_element.get_attribute("src")
            images_list.append(src)
            print(images_list)
        return images_list

    def refresh_until_duplicates(self):
        while True:
            images_list = self.get_lst_elements_on_content_page()
            if len(images_list) > len(set(images_list)):
                Logger.info(f"{self}: Дубликаты не найдены!")
                return images_list
            else:
                Logger.info(f"{self}: Дубликатов пока нет, перезагрузка!")
                self.browser.refresh_page()
