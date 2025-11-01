import time

from config_reader import ConfigReader
from pages.infinity_scroll_page import InfinityScrollPage

config = ConfigReader()


def test_infinity_scroll_down_page(browser):
    infinity_scroll_page = InfinityScrollPage(browser)
    infinity_scroll_page.browser.get(config.base_urls["10_infinity_scroll"])
    infinity_scroll_page.wait_for_open()

    scroll_count = 0

    while scroll_count < 24:
        infinity_scroll_page.browser.scroll_js_down()
        infinity_scroll_page.get_all_scroll_elements()
        scroll_count += 1
