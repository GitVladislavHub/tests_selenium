import os
from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage

from utils.pyautogui_utils import PyautoguiUtils




class UploadDialogWindowPage(BasePage):
    UNIQUE_LOC = "file-submit"
    INPUT_FILE_LOC = "drag-drop-upload"
    CHECK_FILE_LOC = "//*[@id='drag-drop-upload']//div[contains(@class, 'dz-success-mark')]//span"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "UploadDialogWindowPage"
        self.unique_element = Label(browser, self.UNIQUE_LOC, description="Unique element button -> None")
        self.input_file_upload = Button(browser, self.INPUT_FILE_LOC, description="Click Button -> Dialog window")
        self.check_text_loc = Label(browser, self.CHECK_FILE_LOC, description="Get text -> Text")

    def upload_file_dialog_window(self, file_path):
        self.input_file_upload.click()
        absolute_path = os.path.abspath(file_path)
        PyautoguiUtils.upload_file(absolute_path)

    def get_text_upload(self):
        return self.check_text_loc.get_text()
