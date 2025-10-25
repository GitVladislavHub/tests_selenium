from elements.button import Button
from elements.input import Input
from elements.label import Label
from pages.base_page import BasePage


class AlertPage(BasePage):
    AUTH_LOC = "//button[contains(@onclick, 'jsPrompt')]"
    JS_ALERT_LOC = "//button[contains(@onclick, 'jsAlert()')]"
    JS_CONFIRM_LOC = "//button[contains(@onclick, 'jsConfirm()')]"
    JS_PROMPT_LOC = "//button[contains(@onclick, 'jsPrompt()')]"
    LOC_TEXT = "//p[contains(@id, 'result')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Alert_page_js"

        self.authorization_loc = Label(browser, self.AUTH_LOC,
                                       description="unique_loc_element_page")

        self.alert_button = Button(browser, self.JS_ALERT_LOC,
                                   description="Alert Page -> Click Alert Button -> JS Alert")
        self.confirm_button = Button(browser, self.JS_CONFIRM_LOC,
                                     description="Alert Page -> Click Confirm Button -> JS Alert")
        self.promPt_button = Button(browser, self.JS_PROMPT_LOC,
                                    description="Alert Page -> Click Prompt Button -> JS Alert")

        self.js_alert_button = Input(browser, self.JS_ALERT_LOC,
                                     description="Alert Page -> Click Alert Button -> JS Alert")
        self.js_confirm_button = Input(browser, self.JS_CONFIRM_LOC,
                                     description="Alert Page -> Click Alert Button -> JS Alert")
        self.js_promPt_button = Input(browser, self.JS_PROMPT_LOC,
                                     description="Alert Page -> Click Alert Button -> JS Alert")

        self.text_alert_page = Label(browser, self.LOC_TEXT, description="text")
        self.unique_element = self.alert_button

    def click_for_js_alert(self):
        self.alert_button.wait_for_visible()
        self.alert_button.click()

        self.browser.wait_alert_present()
        alert_text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return alert_text

    def is_success_text(self):
        self.text_alert_page.wait_for_visible()
        result_text = self.text_alert_page.get_text()
        return result_text

    def click_for_js_confirm(self):
        self.confirm_button.wait_for_visible()
        self.confirm_button.click()

        self.browser.wait_alert_present()
        alert_text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return alert_text

    def click_for_js_prompt(self, text):
        self.promPt_button.wait_for_visible()
        self.promPt_button.click()

        self.browser.wait_alert_present()
        alert_text = self.browser.get_alert_text()

        if text is not None:
            self.browser.send_keys_alert(text)
        self.browser.accept_alert()
        return alert_text

    def js_click_for_js_alert(self):
        self.js_alert_button.wait_for_visible()
        self.js_alert_button.js_click()
        self.browser.wait_alert_present()

        alert_text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return alert_text

    def js_click_confirm_button(self):
        self.js_confirm_button.wait_for_visible()
        self.js_confirm_button.js_click()
        self.browser.wait_alert_present()

        alert_text = self.browser.get_alert_text()
        self.browser.accept_alert()
        return alert_text

    def js_click_prompt_prompt(self, text):
        self.js_promPt_button.wait_for_visible()
        self.js_promPt_button.js_click()
        self.browser.wait_alert_present()

        alert_text = self.browser.get_alert_text()
        if text is not None:
            self.browser.send_keys_alert(text)
        self.browser.accept_alert()
        return alert_text
