import random
import string

import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture()
def random_email():
    name = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8))
    domain = ["gmail.com", "mail.ru", "icloud.com"]
    return f"{name}@{random.choice(domain)}"


@pytest.fixture()
def random_password(length=9):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))
