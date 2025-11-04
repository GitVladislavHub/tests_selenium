from elements.frame import Frame
from elements.label import Label
from pages.base_page import BasePage


class NestedFramePage(BasePage):
    PAGE_UNIQ_VIS_LOC = "//div[contains(text(), 'Elements')]"
    PARENT_FRAME_LOC = "frame1"  # для ParentFrame(для первого фрейма, для Parent)
    CHILD_FRAME_LOC = "//iframe[contains(@srcdoc, 'Child Iframe')]"  # для ChildFrame(для второго фрейма)
    BODY_TEXT = "//body"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "iframe_page"
        self.parent_iframe_nested = Frame(browser, self.PARENT_FRAME_LOC,
                                          description="Nested Iframe -> None")
        self.child_iframe_nested = Frame(browser, self.CHILD_FRAME_LOC,
                                         description="Nested Iframe -> None")

        self.alert_frame = Label(browser, self.PAGE_UNIQ_VIS_LOC,
                                 description="Iframe Page -> click Button 'Alerts, Frame & Windows'")
        self.unique_element = self.alert_frame

    def get_text_iframe_page_parent(self):
        parent_text_element = Label(self.browser, self.BODY_TEXT, description="Iframe_text -> None")
        text = parent_text_element.get_text()
        return text

    def get_text_iframe_page_child(self):
        parent_text_element = Label(self.browser, self.BODY_TEXT, description="Iframe_text -> None")
        text = parent_text_element.get_text()
        return text
