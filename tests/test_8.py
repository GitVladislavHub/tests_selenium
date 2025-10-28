from config_reader import ConfigReader
from pages.iframe_page import IframePage

config = ConfigReader()


def test_frames(browser):
    frame_page = IframePage(browser)
    frame_page.browser.get(config.base_urls["8_frames"])
    frame_page.wait_for_open()

    frame_page.click_buttons_frames()
