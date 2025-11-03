from elements.button import Button
from elements.label import Label
from pages.base_page import BasePage

from utils.pyautogui_utils import PyautoguiUtils

upload_file_p = PyautoguiUtils()


class UploadDialogWindowPage(BasePage):
    UNIQUE_LOC = "file-submit"
    INPUT_FILE_LOC = "drag-drop-upload"
    CHECK_FILE_LOC = "//div[@id='drag-drop-upload']//div[@class='dz-success-mark']"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "UploadDialogWindowPage"
        self.unique_element = Label(browser, self.UNIQUE_LOC, description="Unique element button -> None")
        self.input_file_upload = Button(browser, self.INPUT_FILE_LOC, description="Click Button -> Dialog window")
        self.check_text_loc = Label(browser, self.CHECK_FILE_LOC, description="Get text -> Text")

    def upload_file_dialog_window(self):
        self.input_file_upload.click()
        upload_file_p.upload_file(r"G:\Projects\tests_selenium\pages\my_image.png")

    def get_text_upload(self):
        return self.check_text_loc.get_text()


    # def upload_file_dialog_window(self):
    #     self.input_file_upload.click()
    #     time.sleep(2)
    #     pyautogui.write(r"G:\Projects\tests_selenium\pages\my_image.png", interval=0.05)
    #     time.sleep(1)
    #     pyautogui.press("enter")
