from faker import Faker
import pytest
from enums import Language
from driver_config import Browser

fake = Faker()


@pytest.fixture()
def random_email():
    return fake.email()


@pytest.fixture()
def random_password():
    return fake.password(length=8)


@pytest.fixture(params=[Language.RU, Language.EN], scope="function")
def lang(request) -> Language:
    return request.param


@pytest.fixture(scope="function")
def driver(lang: Language):
    browser = Browser()
    drv = browser.get(lang)
    yield drv
    browser.quit()
