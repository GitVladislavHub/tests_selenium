from config_reader import ConfigReader
from pages.hovers_page import HoversPage

config = ConfigReader()

def test_hover(browser):
    page_hover = HoversPage(browser)
    page_hover.browser.get(config.base_urls["6_hovers"])
    page_hover.wait_for_open()



