from config_reader import ConfigReader
from pages.dynamic_content_page import DynamicContentPage

config = ConfigReader()


def test_dynamic_content_page(browser):
    dynamic_page = DynamicContentPage(browser)
    dynamic_page.browser.get(config.base_urls["9_dynamic_content"])
    dynamic_page.wait_for_open()

    dynamic_page.refreshing_page_dynamic_content()

