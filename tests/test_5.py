import random

from pages.actions_page import ActionsPage
from config_reader import ConfigReader

config = ConfigReader()


def test_slider(browser):
    page_slider = ActionsPage(browser)
    page_slider.browser.get(config.base_urls["5_actions"])
    page_slider.wait_for_open()

    step = 0.5
    target_value = round(random.uniform(0, 5) / step) * step

    page_slider.action_slider(target_value)
    actual = page_slider.final_value()

    assert actual == target_value, f"Expected: {target_value}, Actual: {actual}"
