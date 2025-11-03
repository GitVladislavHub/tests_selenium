from config_reader import ConfigReader
from pages.upload_dialog_window_page import UploadDialogWindowPage

config = ConfigReader()


def test_upload_dialog_window(browser):
    upload_dialog = UploadDialogWindowPage(browser)
    upload_dialog.browser.get(config.base_urls["11_upload"])
    upload_dialog.wait_for_open()

    upload_dialog.upload_file_dialog_window()

    actual = upload_dialog.get_text_upload()
    expected = "\u2714"
    assert actual == expected
