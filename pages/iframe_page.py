from config_reader import ConfigReader
from elements.button import Button
from pages.base_page import BasePage

config = ConfigReader()


class IframePage(BasePage):
    LOC = ""

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "iframe_page"
        self.alert_frame_windows = Button(browser, self.LOC,
                                          description="Iframe Page -> click Button 'Alerts, Frame & Windows'")
        self.nested_frame_windows = Button(browser, self.LOC,
                                          description="Iframe Page -> click Button 'Alerts, Frame & Windows' -> click button 'Nested Frames'")
        self.unique_element = self.alert_frame_windows

    def click_buttons_frames(self):
        self.alert_frame_windows.wait_for_visible()
