import pytest
from faker import Faker
from selenium import webdriver

from config_reader import ConfigReader

fake = Faker()
config = ConfigReader()

@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture()
def base_auth_url():
    l_and_p = config.base_auth
    base_url = config.base_urls["1_basic_auth"]
    full_url = f"https://{l_and_p['user']}:{l_and_p['password']}@{base_url.replace('https://', '')}"
    return full_url
