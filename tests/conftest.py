from faker import Faker

import pytest
from selenium import webdriver
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
