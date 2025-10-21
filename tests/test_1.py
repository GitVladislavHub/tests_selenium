import pytest
from selenium.webdriver import Keys

from logger.logger import Logger
from pages.main_page_1 import MainLoginPage
from config_reader import ConfigReader

config = ConfigReader()


def test_main_login_page(browser):
    main_page = MainLoginPage(browser)
    main_page.browser.get(config.base_urls["1_basic_auth"])
    main_page.login()

    expected = "Congratulations! You must have the proper credentials."
    actual = main_page.login()
    assert actual == expected, (
        f"Expected: {expected}, "
        f"Actual: {actual}"
    )
