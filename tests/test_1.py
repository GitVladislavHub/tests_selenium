import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

STEAM_GLOBAL_LINK = "https://store.steampowered.com/"
EMAIL_INPUT_KEYBOARD = By.XPATH, '(//input[@type="text"])[2]'  # исправить
PASSWORD_INPUT_KEYBOARD = By.XPATH, '//input[contains(@class, "_2GBWeup5cttgbTw8FM3tfx") and contains(@type, "password")]'
LOGIN_LINK = By.XPATH, "//a[contains(@class, 'global_action_link')]"
TIMEOUT = 12
BUTTON_LOGIN = '//button[contains(@class, "DjSvCZoKKfoNSmarsEcTS")]'


def test_login(browser, random_email, random_password):
    browser.get(STEAM_GLOBAL_LINK)

    click_button = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(LOGIN_LINK))
    click_button.click()

    input_email = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(EMAIL_INPUT_KEYBOARD))
    input_email.send_keys(random_email)

    actual_email = input_email.get_attribute("value")
    expected_email = random_email

    assert actual_email == expected_email, (
        f"Expected:'{expected_email}', Actual: '{actual_email}'"
    )

    input_password = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(PASSWORD_INPUT_KEYBOARD))
    input_password.send_keys(random_password)

    actual_password = input_password.get_attribute("value")
    expected_password = random_password

    assert actual_password == expected_password, (
        f"Expected:'{expected_password}', Actual: '{actual_password}'"
    )

    button_login = browser.find_element(By.XPATH, BUTTON_LOGIN)

    button_login.click()
