import time

from config_reader import ConfigReader
from pages.upload_image_page import UploadImagePage

config = ConfigReader()


def test_upload_image(browser):
    upload_image = UploadImagePage(browser)
    upload_image.browser.get(config.base_urls["11_upload"])
    upload_image.wait_for_open()

    actual = upload_image.upload_image()
    expected = "File Uploaded!"
    assert actual == expected, f"Expected: {expected}, Actual: {actual}"