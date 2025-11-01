import logging
import time
from typing import TYPE_CHECKING

from selenium.common import WebDriverException
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from logger.logger import Logger

if TYPE_CHECKING:
    from elements.base_element import BaseElement


class Browser:
    DEFAULT_TIMEOUT = 10
    PAGE_LOAD_TIMEOUT = 120

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.set_page_load_timeout(self.PAGE_LOAD_TIMEOUT)

        self.main_handle = None

        self._wait = WebDriverWait(self._driver, self.DEFAULT_TIMEOUT)

    @property
    def driver(self) -> WebDriver:
        return self._driver

    def get(self, url: str) -> None:
        Logger.info(f"{self}: get {url}")
        try:
            self._driver.get(url)
        except WebDriverException as err:
            logging.error(f"{self}: {err}")
            raise
        self.main_handle = self._driver.current_window_handle

    def get_current_window_handle(self) -> str:
        """Получить handle текущего окна"""
        return self._driver.current_window_handle

    def get_all_handles(self) -> list:
        """Получить список всех handles"""
        return self._driver.window_handles

    def get_current_title_window(self) -> str:
        """Получить title текущего окна"""
        try:
            title = self._driver.title
            Logger.info(f"{self}: current window title = '{title}'")
            return title
        except WebDriverException as err:
            Logger.error(f"{self}: failed to get window title - {err}")
            raise

    def switch_to_new_window_handle(self, original_handle: str = None) -> str:
        """
        Переключается на новое окно после действия, которое его открывает.
        Возвращает handle оригинального окна для последующего возврата.
        """
        if original_handle is None:
            original_handle = self._driver.current_window_handle

        Logger.info(f"{self}: switching to new window from handle '{original_handle}'")

        new_handle = self.get_new_window_handle(original_handle)

        self.switch_to_window_handle(new_handle)
        Logger.info(f"{self}: switched to new window with handle '{new_handle}'")

        return original_handle

    def close(self) -> None:
        """Закрытие текущего окна/вкладки"""
        Logger.info(f"{self}: close window handle {self.main_handle}")
        self._driver.close()

    def close_tab_by_index(self, index: int) -> None:
        """Закрытие страницы по индексу"""
        handles = self._driver.window_handles
        if index >= len(handles):
            raise IndexError(
                f"Индекс {index} выходит за пределы количества вкладок ({len(handles)})"
            )

        if index < 0:
            raise ValueError(f"Индекс не может быть отрицательным: {index}")
        self._driver.switch_to.window(handles[index])
        self._driver.close()
        if self._driver.window_handles:
            self._driver.switch_to.window(self._driver.window_handles[0])

    def close_tab_by_title(self, title):
        """Закрыть вкладку по title"""
        handles = self.get_all_handles()
        for handle in handles:
            if handle != self.main_handle:
                self.switch_to_window(handle)
                if self.get_current_title_window() == title:
                    self.close()
                    break
        self.switch_to_default_window()

    def close_window_handle(self, handle):
        """Закрыть вкладку по handle"""
        self._driver.switch_to.window(handle)
        self._driver.close()

    def get_new_window_handle(self, original_handle: str) -> str:
        """Появляется новое окно и возвращаем его handle"""
        end_time = time.time() + self.DEFAULT_TIMEOUT
        while time.time() < end_time:
            handles = self._driver.window_handles
            for handle in handles:
                if handle != original_handle:
                    return handle
            time.sleep(0.5)
        raise TimeoutError("Новое окно не появилось")

    def quit(self) -> None:
        """Полный выход из браузера и его закрытие, полное завершение сессии"""
        logging.info(f"{self}: quit")
        try:
            self._driver.quit()
        except WebDriverException as err:
            logging.error(f"{self}: {err}")
            raise

    def execute_script(self, script: str, *args) -> None:
        Logger.info(f"{self}: execute script = '{script}' with args = '{args}'")
        try:
            self._driver.execute_script(script, *args)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def save_screenshot(self, filename: str) -> None:
        Logger.info(f"{self}: save screenshot in '{filename}'")
        self._driver.save_screenshot(filename=filename)

    def switch_to_default_window(self) -> None:
        """Вернуться на базовое(первоначальное) окно"""
        Logger.info(f"{self}: switch to default window")
        try:
            self._driver.switch_to.window(self.main_handle)
        except WebDriverException as err:
            Logger.error(f"{self}: {err}")
            raise

    def switch_to_window_handle(self, handle: str) -> None:
        """Переключиться на окно по handle"""
        Logger.info(f"{self}: switch to window with handle '{handle}'")
        self._driver.switch_to.window(handle)

    def switch_to_window(self, title: str) -> None:
        """Переключиться на любое необходимое окно по title"""
        Logger.info(f"{self}: switch to window with title '{title}'")
        end_time = time.time() + self.PAGE_LOAD_TIMEOUT
        while True:
            handles = self._driver.window_handles
            for handle in handles:
                self._driver.switch_to.window(handle)
                if self._driver.title == title:
                    Logger.info(f"{self}: new window handle = {self._driver.current_window_handle}")
                    return
            if time.time() < end_time:
                time.sleep(1)
            else:
                Logger.error(f"{self}: window with title '{title}' wasn't found")
                raise ValueError(f"window with title '{title}' wasn't found")

    def wait_alert_present(self):
        Logger.info(f"{self}: wait alert present")
        return self._wait.until(expected_conditions.alert_is_present())

    def switch_to_alert(self):
        Logger.info(f"{self}: switch to alert")
        self.wait_alert_present()
        return self.driver.switch_to.alert

    def get_alert_text(self):
        Logger.info(f"{self}: get alert text")
        return self.switch_to_alert().text

    def accept_alert(self):
        Logger.info(f"{self}: accept alert")
        self.switch_to_alert().accept()

    def send_keys_alert(self, text: str):
        Logger.info(f"{self}: send '{text}' to alert")
        self.switch_to_alert().send_keys(text)

    def switch_to_frame(self, frame: "BaseElement"):
        Logger.info(f"{self}: switch to frame")
        return self.driver.switch_to.frame(frame.wait_for_presence())

    def switch_to_default_content(self):
        Logger.info(f"{self}: switch to default content")
        self.driver.switch_to.default_content()

    def go_back(self):
        """Вернуться на предыдущую страницу в истории браузера.(открыта одна вкладка, на несколько вкладок не работает)"""
        Logger.info(f"{self}: navigating back")
        self.driver.back()
        Logger.info(f"{self}: successfully navigated back")
        return True

    def refresh_page(self):
        Logger.info(f"{self}: refreshing page...")
        self._driver.refresh()
        Logger.info(f"{self}: refreshing page successfully")

    def scroll_js_down(self):
        Logger.info(f"{self}: scrolling js down")
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}_{self._driver.session_id}"

    def __repr__(self) -> str:
        return str(self)
