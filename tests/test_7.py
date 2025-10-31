import time

from config_reader import ConfigReader
from pages.handlers_page import HandlersPage
from pages.new_window_page import NewWindowPage

config = ConfigReader()


def test_handlers_clicks(browser):
    handlers_page = HandlersPage(browser)
    handlers_page.browser.get(config.base_urls["7_handlers"])
    handlers_page.wait_for_open()

    main_window = browser.switch_to_new_window_handle()

    new_window_page = NewWindowPage(browser)
    new_window_page.wait_for_open()

    actual = new_window_page.get_text_page()
    expected = "New Window"
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    browser.switch_to_window_handle(main_window)

    actual = handlers_page.get_text_element()
    expected = "Opening a new window"
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    handlers_page.click_href_button_handler()

    new_window_page.wait_for_open()
    browser.switch_to_new_window_handle()

    actual = new_window_page.get_text_page()
    expected = "New Window"
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"

    browser.switch_to_new_window_handle()
    handlers_page.wait_for_open()

    browser.close_tab_by_index(1)

    browser.close_tab_by_index(1)
