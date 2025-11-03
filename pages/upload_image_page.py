import time

from elements.input import Input
from elements.label import Label
from pages.base_page import BasePage
import os


class UploadImagePage(BasePage):
    UNIQUE_ELEMENT_LOC = "file-submit"
    BUTTON_IMAGE_LOC = "file-submit"
    DRAG_DROP_LOC = "drag-drop-upload"
    BUTTON_UPLOAD_LOC = "file-upload"

    TEXT_UPLOADED_LOC = "//h3[contains(text(), 'File Uploaded')]"

    def __init__(self, browser):
        super().__init__(browser)
        self.page_name = "Upload Image"

        self.unique_element = Input(browser, self.UNIQUE_ELEMENT_LOC, description="Upload page -> None")
        self.button_upload = Input(browser, self.BUTTON_UPLOAD_LOC, description="Click button -> Upload success page")
        self.drag_and_drop = Input(browser, self.DRAG_DROP_LOC, description="Upload file -> None")
        self.button_image = Input(browser, self.BUTTON_IMAGE_LOC, description="Upload file -> None")
        self.text_uploaded_loc = Label(browser, self.TEXT_UPLOADED_LOC, description="Upload file -> None")

    def upload_image(self):
        file_path = os.path.abspath("resources/my_image.png")
        self.button_upload.send_keys_upload_file(file_path)
        self.button_image.click()
        self.text_uploaded_loc.wait_for_visible()
        text = self.text_uploaded_loc.get_text()
        return text
