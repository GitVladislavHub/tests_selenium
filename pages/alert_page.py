from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage
from logger.logger import Logger
from faker import Faker

fake = Faker()


class AlertPage(BasePage):
    AUTH_LOC = ("//button[contains(@onclick, 'jsPrompt') "
                "or contains(@onclick, 'jsConfirm') "
                "or contains(@onclick, 'jsAlert')]")
    JS_ALERT_LOC = "//button[contains(@onclick, 'jsAlert()')]"
    JS_CONFIRM_LOC = "//button[contains(@onclick, 'jsConfirm()')]"
    JS_PROMPT_LOC = "//button[contains(@onclick, 'jsPrompt()')]"
    LOC_TEXT = "//p[contains(@id, 'result')]"
    TEXT_FAKER = fake.text(max_nb_chars=10)

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Alert_page_1"

        self.unique_loc_element = Label(browser, self.AUTH_LOC, description="unique_loc_element_page")

        self.js_alert_button = Button(browser, self.JS_ALERT_LOC, description="button_for_js_alert")
        self.js_confirm_button = Button(browser, self.JS_CONFIRM_LOC, description="button_for_js_confirm")
        self.js_promPt_button = Button(browser, self.JS_PROMPT_LOC, description="button_for_js_prompt")

        self.unique_element_text = Label(browser, self.LOC_TEXT, description="text")

    def success_open(self):
        Logger.info(f"{self} success open")
        self.unique_loc_element.wait_for_visible()

    def click_for_js_alert(self):
        self.js_alert_button.wait_for_visible()
        self.js_alert_button.click()

        self.browser.wait_alert_present()
        alert_text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return alert_text

    def is_success_text(self):
        self.unique_element_text.wait_for_visible()
        result_text = self.unique_element_text.get_text()
        return result_text

    def click_for_js_confirm(self):
        self.js_confirm_button.wait_for_visible()
        self.js_confirm_button.click()

        self.browser.wait_alert_present()
        alert_text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return alert_text

    def is_success_text_confirm(self):
        self.unique_element_text.wait_for_visible()
        result_text = self.unique_element_text.get_text()
        return result_text

    def click_for_js_prompt(self):
        self.js_promPt_button.wait_for_visible()
        self.js_promPt_button.click()

        self.browser.wait_alert_present()
        alert_text = self.browser.get_alert_text()
        self.browser.send_keys_alert(self.TEXT_FAKER)
        self.browser.accept_alert()
        return alert_text

    def is_success_text_prompt(self):
        self.unique_element_text.wait_for_visible()
        result_text = self.unique_element_text.get_text()
        return result_text
