import pytest
from browser.browser import Browser
from browser.browser_factory import BrowserFactory


@pytest.fixture(scope="function")
def browser():
    options = ["--window-size=1920,1080"]
    driver = BrowserFactory.get_driver(options=options)
    browser = Browser(driver)
    yield browser
    browser.quit()
