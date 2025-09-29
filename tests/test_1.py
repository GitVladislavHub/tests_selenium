
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

def test_login(open_browser):
    browser = open_browser
    browser.get("https://store.steampowered.com/")

    click_button = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(@class, 'global_action_link')]"))
    )
    click_button.click()

    browser.get("https://store.steampowered.com/login/?redir=&redir_ssl=1")

    input_keyboard = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//input[contains(@class, "_2GBWeup5cttgbTw8FM3tfx") and contains(@type, "text")]'))
    )
    input_keyboard.send_keys('vladislav.selenium@gmail.com')

    input_password = WebDriverWait(browser, 3).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//input[contains(@class, "_2GBWeup5cttgbTw8FM3tfx") and contains(@type, "password")]')
        )
    )
    input_password.send_keys('123456789')


    button_login = browser.find_element(By.XPATH, '//button[contains(@class, "DjSvCZoKKfoNSmarsEcTS")]')

    button_login.click()

    time.sleep(5)
