from config_reader import ConfigReader
from pages.dynamic_content_page import DynamicContentPage

config = ConfigReader()


def test_dynamic_content_page(browser):
    dynamic_page = DynamicContentPage(browser)
    dynamic_page.browser.get(config.base_urls["9_dynamic_content"])
    dynamic_page.wait_for_open()

    dynamic_page.get_lst_elements_on_content_page()

    duplicate_images = dynamic_page.refresh_until_duplicates()
    assert len(duplicate_images) > 0, "Должен быть дубликат!"
