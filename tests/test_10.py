from config_reader import ConfigReader
from pages.infinity_scroll_page import InfinityScrollPage

config = ConfigReader()


def test_infinity_scroll_down_page(browser):
    infinity_scroll_page = InfinityScrollPage(browser)
    infinity_scroll_page.browser.get(config.base_urls["10_infinity_scroll"])
    infinity_scroll_page.wait_for_open()

    age = 24
    index = 1
    while index <= age:
        current = infinity_scroll_page.get_element_by_index(index)
        current.wait_for_presence()
        last_web_el = current.get_web_element()
        browser.driver.execute_script("arguments[0].scrollIntoView();", last_web_el)
        index += 1
