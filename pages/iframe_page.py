from config_reader import ConfigReader
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage

config = ConfigReader()


class IframePage(BasePage):
    PAGE_UNIQ_VIS_LOC = "//div[@class='header-text' and text()='Elements']"
    CLICK_ALERTS_LOC = "//div[contains(text(), 'Alerts, Frame & Windows')]"
    NESTED_FRAMES_LOC = "//span[text()='Nested Frames']"
    NESTED_IFRAME_LOC = "frame1"  # для ParentFrame(для первого фрейма, для Parent)
    CHILD_FRAME_LOC = "//iframe[contains(@srcdoc, 'Child Iframe')]"  # для ChildFrame(для второго фрейма)
    BODY_TEXT = "//body"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "iframe_page"
        self.alerts_frame_window = Button(browser, self.CLICK_ALERTS_LOC,
                                          description="Iframe Page -> click Button Alerts, Frame & Windows -> Buttons")
        self.nested_frame = Button(browser, self.NESTED_FRAMES_LOC,
                                   description="click button 'Nested Frames' -> Form 'Nested Frames'")
        self.parent_iframe_nested = Label(browser, self.NESTED_IFRAME_LOC,
                                          description="Nested Iframe -> None")
        self.child_iframe_nested = Label(browser, self.CHILD_FRAME_LOC,
                                         description="Nested Iframe -> None")

        self.alert_frame = Label(browser, self.PAGE_UNIQ_VIS_LOC,
                                 description="Iframe Page -> click Button 'Alerts, Frame & Windows'")
        self.unique_element = self.alert_frame

    def click_buttons_frames(self):
        self.alerts_frame_window.click()
        self.nested_frame.click()

    def get_text_iframe_page(self):
        self.browser.switch_to_frame(self.parent_iframe_nested)

        parent_text_element = Label(self.browser, self.BODY_TEXT, description="Iframe_text -> None")
        text = parent_text_element.get_text()
        self.browser.switch_to_default_content()
        return text

    def get_text_iframe_page_child(self):
        self.browser.switch_to_frame(self.child_iframe_nested)
        parent_text_element = Label(self.browser, self.BODY_TEXT, description="Iframe_text -> None")
        text = parent_text_element.get_text()
        self.browser.switch_to_default_content()
        return text
