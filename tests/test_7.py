from config_reader import ConfigReader
from pages.handlers_page import HandlersPage

config = ConfigReader()


def test_handlers_clicks(browser):
    page_handlers = HandlersPage(browser)
    page_handlers.browser.get(config.base_urls["7_handlers"])
    page_handlers.wait_for_open()
    actual = page_handlers.click_href_button_handler()
    expected = "New Window"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    page_handlers.back_on_page()

    actual = page_handlers.click_href_button_handler()
    expected = "New Window"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    actual = page_handlers.back_on_page()
    expected = "Click Here"
    assert actual == expected, f"expected: {expected}, actual: {actual}"

    page_handlers.close_pages()
