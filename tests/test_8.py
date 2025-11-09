from config_reader import ConfigReader
from pages.iframe_page import IframePage
from pages.nested_frame_page import NestedFramePage

config = ConfigReader()


def test_frames(browser):
    frame_page = IframePage(browser)
    frame_page.browser.get(config.base_urls["8_frames"])
    frame_page.wait_for_open()

    frame_page.click_buttons_frames()

    nested_frames = NestedFramePage(browser)
    nested_frames.wait_for_open()

    browser.switch_to_frame(nested_frames.parent_iframe_nested)

    actual = nested_frames.get_text_iframe_page_parent()
    expected = "Parent frame"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    browser.switch_to_frame(nested_frames.child_iframe_nested)

    actual = nested_frames.get_text_iframe_page_child()
    expected = "Child Iframe"
    assert actual == expected, f"Expected: {expected}, "f"Actual: {actual}"

    browser.switch_to_default_content()
