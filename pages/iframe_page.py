from config_reader import ConfigReader
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage

config = ConfigReader()


class IframePage(BasePage):
    PAGE_UNIQ_VIS_LOC = "//div[contains(text(), 'Elements')]"
    CLICK_ALERTS_LOC = "//div[contains(text(), 'Alerts, Frame & Windows')]"
    NESTED_FRAMES_LOC = "//span[contains(text(), 'Nested Frames')]"
    BODY_TEXT = "//body"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "iframe_page"
        self.alerts_frame_window = Button(browser, self.CLICK_ALERTS_LOC,
                                          description="Iframe Page -> click Button Alerts, Frame & Windows -> Buttons")
        self.nested_frame = Button(browser, self.NESTED_FRAMES_LOC,
                                   description="click button 'Nested Frames' -> Form 'Nested Frames'")

        self.alert_frame = Label(browser, self.PAGE_UNIQ_VIS_LOC,
                                 description="Iframe Page -> click Button 'Alerts, Frame & Windows'")
        self.unique_element = self.alert_frame

    def click_buttons_frames(self):
        self.alerts_frame_window.click()
        self.nested_frame.click()
