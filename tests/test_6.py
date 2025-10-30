import time

from config_reader import ConfigReader
from pages.hovers_page import HoversPage
from pages.view_profile_page import ViewProfilePage

config = ConfigReader()


def test_hover(browser):
    page_hover = HoversPage(browser)
    page_hover.browser.get(config.base_urls["6_hovers"])
    page_hover.wait_for_open()

    page_hover_main = page_hover.browser.get_current_window_handle()

    actual = page_hover.get_text_hover_element(browser, 1)
    expected = "name: user1"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    page_hover.click_view_profile(browser, user_index=1)

    view_profile_page = ViewProfilePage(browser)
    view_profile_page.wait_for_open()

    view_profile_page_main = view_profile_page.browser.get_current_window_handle()

    actual = view_profile_page.get_text_view_profile()
    expected = "Sinatra doesn’t know this ditty."
    assert actual == expected

    browser.go_back()

    page_hover.wait_for_open()

    actual = page_hover.get_text_hover_element(browser, 2)
    expected = "name: user2"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    page_hover.click_view_profile(browser, user_index=2)

    view_profile_page = ViewProfilePage(browser)
    view_profile_page.wait_for_open()

    actual = view_profile_page.get_text_view_profile()
    expected = "Sinatra doesn’t know this ditty."
    assert actual == expected

    browser.go_back()

    page_hover.wait_for_open()

    actual = page_hover.get_text_hover_element(browser, 3)
    expected = "name: user3"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    page_hover.click_view_profile(browser, user_index=3)

    view_profile_page = ViewProfilePage(browser)
    view_profile_page.wait_for_open()

    actual = view_profile_page.get_text_view_profile()
    expected = "Sinatra doesn’t know this ditty."
    assert actual == expected

    browser.go_back()

    page_hover.wait_for_open()
