import time

from config_reader import ConfigReader
from pages.handlers_page import HandlersPage

config = ConfigReader()


def test_handlers_clicks(browser):
    page_handlers = HandlersPage(browser)
    page_handlers.browser.get(config.base_urls["7_handlers"])
    page_handlers.wait_for_open()

    actual = page_handlers.click_href_button_handler()
    expected = "New Window"
    assert actual == expected

    browser.switch_to_default_window()

    actual = page_handlers.click_href_button_handler()
    expected = "New Window"
    assert actual == expected

    browser.switch_to_default_window()
    actual = page_handlers.click_window_href_button.get_text()
    expected = "Click Here"
    assert actual == expected

    browser.close_tab_by_index(2)

    browser.switch_to_default_window()
    actual = page_handlers.click_window_href_button.get_text()
    expected = "Click Here"
    assert actual == expected

    browser.close_tab_by_index(1)

    browser.switch_to_default_window()
    actual = page_handlers.click_window_href_button.get_text()
    expected = "Click Here"
    assert actual == expected
