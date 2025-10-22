import pytest
from browser.browser import Browser
from browser.browser_factory import BrowserFactory
from config_reader import ConfigReader

config = ConfigReader()

@pytest.fixture(scope="function")
def browser():
    driver = BrowserFactory.get_driver()
    browser = Browser(driver)
    window_size = config.pc_window_size
    browser.driver.set_window_size(
        window_size["width"],
        window_size["height"]
    )
    yield browser
    browser.quit()
