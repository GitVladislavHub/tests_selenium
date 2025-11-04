from config_reader import ConfigReader
from pages.hovers_page import HoversPage
from pages.view_profile_page import ViewProfilePage

config = ConfigReader()


def test_hover(browser):
    page_hover = HoversPage(browser)
    page_hover.browser.get(config.base_urls["6_hovers"])
    page_hover.wait_for_open()

    for user_index in [1, 2, 3]:
        actual = page_hover.get_text_hover_element(browser, user_index)
        expected = f"name: user{user_index}"
        assert actual == expected

        page_hover.click_view_profile(browser, user_index)

        view_profile_page = ViewProfilePage(browser)
        view_profile_page.wait_for_open()
        actual = view_profile_page.get_text_view_profile()
        expected = "Sinatra doesn’t know this ditty."
        assert actual == expected, f"Текст не совпадает! Ожидалось: '{expected}', получено: '{actual}'"

        if user_index < 3:
            browser.go_back()
            page_hover.wait_for_open()
