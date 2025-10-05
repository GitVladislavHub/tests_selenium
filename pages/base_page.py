from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT_2 = 10


class BasePage:
    SEARCH_LOCATOR = By.XPATH, "//input[contains(@type, 'text') and contains(@role, 'combobox')]"
    URL_HOME_STEAM = "https://store.steampowered.com/"
    SEARCH_BUTTON = (By.XPATH, "//form[contains(@role, 'search')]//button[contains(@type, 'submit')]")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL_HOME_STEAM)
        return self

    def click(self, locator):
        click_search = WebDriverWait(self.driver, TIMEOUT_2).until(EC.element_to_be_clickable(locator))
        click_search.click()
        return self

    def input_text_steam(self, locator, text):
        element = WebDriverWait(self.driver, TIMEOUT_2).until(EC.visibility_of_element_located(locator))
        element.send_keys(text)
        return self

    def search_button(self, locator):
        click_button = WebDriverWait(self.driver, TIMEOUT_2).until(EC.element_to_be_clickable(locator))
        click_button.click()

    def visible_unique_element(self, locator):
        try:
            WebDriverWait(self.driver, TIMEOUT_2).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False
