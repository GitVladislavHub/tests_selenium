import time

from config_reader import ConfigReader
from pages.infinity_scroll_page import InfinityScrollPage

config = ConfigReader()


def test_infinity_scroll_down_page(browser):
    infinity_scroll_page = InfinityScrollPage(browser)
    infinity_scroll_page.browser.get(config.base_urls["10_infinity_scroll"])
    infinity_scroll_page.wait_for_open()

    infinity_scroll_page.get_all_scroll_elements()



