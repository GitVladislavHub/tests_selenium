import random

from pages.actions_page import ActionsPage
from config_reader import ConfigReader

config = ConfigReader()


def test_slider(browser):
    page_slider = ActionsPage(browser)
    page_slider.browser.get(config.base_urls["5_actions"])
    page_slider.wait_for_open()

    min_val, max_val, step = page_slider.get_slider_bounds()
    target_value = round(random.uniform(min_val, max_val) / step) * step

    page_slider.action_slider(target_value)
    actual = page_slider.get_text_final_value()

    assert actual == target_value, f"Expected: {target_value}, Actual: {actual}"
