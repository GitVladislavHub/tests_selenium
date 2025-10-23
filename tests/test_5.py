from pages.actions_page import ActionsPage
from config_reader import ConfigReader

config = ConfigReader()


def test_slider(browser):
    page_slider = ActionsPage(browser)
    page_slider.browser.get(config.base_urls["5_actions"])
    page_slider.wait_for_open()

    actual = page_slider.action_slider()
    expected = page_slider.value_slider_final()
    assert actual == expected , "Ошибка: значения отличаются!"

