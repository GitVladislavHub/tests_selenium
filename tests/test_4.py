from faker import Faker

from config_reader import ConfigReader
from pages.context_click_alert import ContextClickAlert

config = ConfigReader()
fake = Faker()


def test_context_click_alert(browser):
    page_alert_click = ContextClickAlert(browser)
    page_alert_click.browser.get(config.base_urls["4_alerts_context"])
    page_alert_click.wait_for_open()

    actual = page_alert_click.right_click_context_menu()
    expected = "You selected a context menu"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"
