from faker import Faker
import pytest
from selenium import webdriver

from driver_config import Browser

fake = Faker()


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def random_email():
    return fake.email()


@pytest.fixture()
def random_password():
    return fake.password(length=8)


@pytest.fixture(params=["ru", "en"], scope="function")
def lang(request):
    return request.param


@pytest.fixture(scope="function")
def driver(lang):
    browser = Browser()
    drv = browser.get(lang)
    yield drv
    browser.quit()
