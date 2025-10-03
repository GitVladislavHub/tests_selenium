from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

STEAM_GLOBAL_LINK = "https://store.steampowered.com/"
EMAIL_INPUT_KEYBOARD = By.XPATH, '(//input[@type="text"])[2]'
PASSWORD_INPUT_KEYBOARD = By.XPATH, '//input[contains(@type, "password")]'
LOGIN_LINK = By.XPATH, "//a[contains(@class, 'global_action_link')]"
TIMEOUT = 12
BUTTON_LOGIN = '//button[contains(@type, "submit") and contains(text(), "Войти")]'
CAROUSEL_ITEMS = By.XPATH, ("//div[contains(@class,'carousel_items') and contains(@class,'store_capsule_container') "
                            "and contains(@class,'responsive_scroll_snap_ctn') and contains(@class,'hero_row')]")
CREATE_ACCOUNT = By.XPATH, ("//a[contains(@class,'login_create_btn') and contains(@class,'btn_blue_steamui') "
                            "and contains(@class,'btn_medium')]")
WARNING = By.XPATH, "//form[.//input[contains(@type,'password')]]//a[contains(@href,'HelpWithLogin')]/preceding-sibling::div[1]"
LOADING_BUTTON = By.XPATH, '//button[@type="submit" and @disabled]/div[1]/div[1]'


def test_login(browser, random_email, random_password):
    browser.get(STEAM_GLOBAL_LINK)
    home_page = WebDriverWait(browser, TIMEOUT).until(EC.visibility_of_element_located(CAROUSEL_ITEMS))

    assert home_page.is_enabled(), "Главная страница еще не загрузилась"

    click_button = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(LOGIN_LINK))
    click_button.click()

    login_page = WebDriverWait(browser, TIMEOUT).until(EC.visibility_of_element_located(EMAIL_INPUT_KEYBOARD))

    assert login_page.is_displayed(), "Ошибочка: открылась другая страница."

    input_email = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(EMAIL_INPUT_KEYBOARD))
    input_email.send_keys(random_email)

    input_password = WebDriverWait(browser, TIMEOUT).until(EC.element_to_be_clickable(PASSWORD_INPUT_KEYBOARD))
    input_password.send_keys(random_password)

    button_login = browser.find_element(By.XPATH, BUTTON_LOGIN)
    button_login.click()

    loading_element = WebDriverWait(browser, TIMEOUT).until(EC.visibility_of_element_located(LOADING_BUTTON))

    assert loading_element.is_enabled(), "Значок загрузки не появился"

    warning_error = WebDriverWait(browser, TIMEOUT).until(EC.visibility_of_element_located(WARNING))

    assert warning_error.text in 'Пожалуйста, проверьте свой пароль и имя аккаунта и попробуйте снова.', "Не тот текст"
