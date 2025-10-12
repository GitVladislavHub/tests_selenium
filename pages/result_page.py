from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from pages.base_page import BasePage


class ResultPage(BasePage):
    FILTER_BUTTON = (By.XPATH,
                     "//button[contains(@class, 'trigger') and contains(@id, 'sort_by_trigger')]")  # Кнопка сортировки(релевантность)
    DROPDOWN_CONTAINER = (By.XPATH,
                          "//div[contains(@id,'sort_by_list') or contains(@id,'sort_by_droplist')]")  # Кнопка нажата(меню выбора)
    DECREASING_ELEMENT = (By.XPATH,
                          "//*[contains(@id,'sort_by_droplist')]//a[contains(@id,'Price_DESC')]")  # Кнопка сортировки(убывание цены)
    MENU_ELEMENTS = (By.XPATH, "//*[contains(@id,'sort_by_droplist')]")  # Выпадающий список элементов
    FIRST_ELEMENT = (By.XPATH, "//a[contains(@class,'search_result_row')][1]")

    PRICE = (By.XPATH, "//*[contains(@class,'discount_final_price')]")

    ALL_PRICES = (By.CSS_SELECTOR, "a.search_result_row div.discount_final_price")

    SEARCH_PANEL = (By.XPATH, "//input[@id='term']")
    LOADER_BACKGROUND_LOC = (By.XPATH, "//div[@id='search_result_container' and contains(@style, 'opacity: 0.5')]")

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
        self.fast_wait.until(EC.visibility_of_element_located(self.LOADER_BACKGROUND_LOC))
        self.fast_wait.until_not(EC.visibility_of_element_located(self.LOADER_BACKGROUND_LOC))

    def give_me_prices(self, limit_prices):
        prices = self.wait.until(EC.presence_of_all_elements_located(self.ALL_PRICES))
        all_prices = []
        for p in prices:
            lines = p.text.splitlines()
            text = lines[-1].replace("€", "").replace(",", ".").strip()
            try:
                price = float(text)
            except ValueError:
                price = 0.0
            all_prices.append(price)
            if len(all_prices) >= limit_prices:
                break
        return all_prices
