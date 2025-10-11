from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage



class ResultPage(BasePage):
    FILTER_BUTTON = (By.XPATH, "//button[contains(@class, 'trigger') and contains(@id, 'sort_by_trigger')]")  # Кнопка сортировки(релевантность)
    DROPDOWN_CONTAINER = (By.XPATH, "//div[contains(@id,'sort_by_list') or contains(@id,'sort_by_droplist')]")  # Кнопка нажата(меню выбора)
    DECREASING_ELEMENT = (By.XPATH, "//*[contains(@id,'sort_by_droplist')]//a[contains(@id,'Price_DESC')]")  # Кнопка сортировки(убывание цены)
    MENU_ELEMENTS = (By.XPATH, "//*[contains(@id,'sort_by_droplist')]")  # Выпадающий список элементов
    FIRST_ELEMENT = (By.XPATH, "//a[contains(@class,'search_result_row')][1]")

    PRICE = (By.XPATH, "//*[contains(@class,'discount_final_price')]")

    BLOCK = (By.XPATH, "//div[contains(@class,'discount_final_price')]")
    DISCOUNT_BLOCK = (By.XPATH, "//div[contains(@class,'your_price_label')]/following-sibling::div[1]")
    SEARCH_PANEL = (By.XPATH, "//input[@id='term']")


    def wait_success_open_page(self):
        return self.wait.until(EC.visibility_of_element_located(self.FILTER_BUTTON))

    def filter_button(self):
        f_button = self.wait.until(EC.element_to_be_clickable(self.FILTER_BUTTON))
        f_button.click()
        return self

    def reduce_the_price(self):
        r_price = self.wait.until(EC.element_to_be_clickable(self.DECREASING_ELEMENT))
        r_price.click()
        return self

    def wait_until_results_updated(self):
        old_first = self.wait.until(EC.presence_of_element_located(self.FIRST_ELEMENT))
        self.wait.until(EC.staleness_of(old_first))
        self.wait.until(EC.presence_of_element_located(self.FIRST_ELEMENT))
        return self

    def games_filter(self, limit_prices):
        prices = (
                self.wait.until(EC.presence_of_all_elements_located(self.BLOCK)) +
                self.wait.until(EC.presence_of_all_elements_located(self.DISCOUNT_BLOCK))
        )
        all_prices = []
        for p in prices:
            lines = p.text.splitlines()
            text = lines[-1].replace("€", "").replace(",", ".").strip()
            all_prices.append(float(text))
            if len(all_prices) >= limit_prices:
                break
        return sorted(all_prices, reverse=True)
