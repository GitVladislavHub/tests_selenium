import time

from faker import Faker

from config_reader import ConfigReader
from pages.alert_page import AlertPage

config = ConfigReader()
fake = Faker()

def test_alerts_js(browser):
    page_alert_js = AlertPage(browser)
    page_alert_js.browser.get(config.base_urls["2_java_script_alerts"])
    page_alert_js.open_success_page()
    test_text = fake.text(max_nb_chars=10)

    actual = page_alert_js.js_click_for_js_alert()
    expected = "I am a JS Alert"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_alert_js.is_success_text()
    expected = "You successfully clicked an alert"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_alert_js.js_click_confirm_button()
    expected = "I am a JS Confirm"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_alert_js.is_success_text()
    expected = "You clicked: Ok"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_alert_js.js_click_prompt_prompt(text=test_text)
    expected = "I am a JS prompt"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    actual = page_alert_js.is_success_text()
    expected = f"You entered: {test_text}"
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"