from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC

class HomePage(BasePage):
    BASE_AUTH_LOC = (By.XPATH, "//p[contains(text(), 'Congratulations')]")
    SUCCESS_AUTH_LOC = (By.XPATH, "//h3[contains(text(), 'Basic Auth')]")

    def authorization_success(self):
        return self.wait.until(EC.visibility_of_element_located(self.BASE_AUTH_LOC))

    def is_success_open_page(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUCCESS_AUTH_LOC))