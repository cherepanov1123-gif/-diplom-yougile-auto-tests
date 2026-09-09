"""
Модуль с базовым классом для всех Page Object'ов.
"""

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Базовый класс для страниц. Содержит общие методы для работы с драйвером.
    """

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click(self, locator: tuple):
        """
        Кликает по элементу с ожиданием его кликабельности.

        :param locator: Кортеж (By, selector).
        """
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def send_keys(self, locator: tuple, text: str):
        """
        Вводит текст в поле с ожиданием его видимости.

        :param locator: Кортеж (By, selector).
        :param text: Текст для ввода.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator: tuple) -> str:
        """
        Возвращает текст элемента.

        :param locator: Кортеж (By, selector).
        :return: Текст элемента.
        """
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text
