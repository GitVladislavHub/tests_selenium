import time
from config_reader import ConfigReader
from pages.alert_page import AlertPage

config = ConfigReader()


def test_alerts(browser):
    page_alert = AlertPage(browser)
    page_alert.browser.get(config.base_urls["2_java_script_alerts"])
    page_alert.success_open()
    page_alert.click_for_js_alert()

    expected = "I am a JS Alert"
    actual = page_alert.click_for_js_alert()
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_alert.is_success_text()
    expected = "You successfully clicked an alert"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    expected = "I am a JS Confirm"
    actual = page_alert.click_for_js_confirm()
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_alert.is_success_text_confirm()
    expected = "You clicked: Ok"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_alert.click_for_js_prompt()
    expected = "I am a JS prompt"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_alert.is_success_text_prompt()
    expected = f"You entered: {page_alert.TEXT_FAKER}"
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"
