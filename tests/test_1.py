import pytest

from config_reader import ConfigReader
from pages.home_page import HomePage

config = ConfigReader()


def test_basic_authorization(driver, base_auth_url):
    home_page = HomePage(driver)

    home_page.driver.get(base_auth_url)

    home_page.authorization_success()
    assert home_page.is_success_open_page(), (
        "Ошибка: страница не открылась! "
        "Ожидалось: заголовок 'Basic Auth' должен быть видимым."
    )
    message = home_page.authorization_success().text
    assert "Congratulations! You must have the proper credentials." in message, "Авторизация не выполнена!"
