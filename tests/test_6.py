from config_reader import ConfigReader
from pages.hovers_page import HoversPage

config = ConfigReader()


def test_hover(browser):
    page_hover = HoversPage(browser)
    page_hover.browser.get(config.base_urls["6_hovers"])
    page_hover.wait_for_open()

    actual = page_hover.get_text_hover_element(browser, 1)
    expected = "name: user1"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_hover.go_on_hovers_page()
    assert actual, f"Expected: Страница успешно открыта! , "f"Actual: {actual}"
