import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

STEAM_GLOBAL_LINK = "https://store.steampowered.com/"
EMAIL_INPUT_KEYBOARD = By.XPATH, '(//input[@type="text"])[2]'
PASSWORD_INPUT_KEYBOARD = By.XPATH, '//input[contains(@type, "password")]'
LOGIN_LINK = By.XPATH, "//a[contains(@class, 'global_action_link')]"
TIMEOUT = 12
BUTTON_LOGIN = '//button[contains(@type, "submit") and contains(text(), "Войти")]'
CAROUSEL_ITEMS = By.XPATH, "//div[@aria-label='ИЗБРАННЫЕ ПРЕДЛОЖЕНИЯ']"
CREATE_ACCOUNT = By.XPATH, '//a[contains(@class, "login_create_btn btn_blue_steamui btn_medium")]'
TEXT_WARNING = By.XPATH, "//div[contains(text(), 'проверьте свой пароль и имя аккаунта')]"


def test_login(browser, random_email, random_password):
    browser.get(STEAM_GLOBAL_LINK)
    home_page = WebDriverWait(browser, TIMEOUT).until(EC.visibility_of_element_located(CAROUSEL_ITEMS))

    assert home_page.is_displayed(), "Главная страница еще не загрузилась"

    click_button = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(LOGIN_LINK))
    click_button.click()

    assert "/login" in browser.current_url, "Ошибка: не та страница!"

    input_email = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(EMAIL_INPUT_KEYBOARD))
    input_email.send_keys(random_email)

    input_password = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(PASSWORD_INPUT_KEYBOARD))
    input_password.send_keys(random_password)

    button_login = browser.find_element(By.XPATH, BUTTON_LOGIN)
    button_login.click()



    text_error = WebDriverWait(browser, TIMEOUT).until(EC.visibility_of_element_located(TEXT_WARNING))

    assert text_error.is_displayed(), "Текст предупреждения не появился"

    time.sleep(2)
