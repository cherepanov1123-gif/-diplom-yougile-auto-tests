"""
Модуль с классом для страницы авторизации YouGile.
"""

import time
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pages.main_page import MainPage
from pages.base_page import BasePage


class LoginPage(BasePage):
    """
    Класс для страницы авторизации YouGile.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://ru.yougile.com/team/"
        self.wait = WebDriverWait(driver, 30)

    @allure.step("Открыть страницу авторизации")
    def open(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        time.sleep(3)
        return self

    @allure.step("Войти с логином '{login}' и паролем")
    def login(self, login: str, password: str):
        # Ждём загрузки страницы
        self.wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        time.sleep(3)

        # Поле для ввода email
        login_input = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[contains(@placeholder, 'mail')]")
            )
        )
        login_input.clear()
        login_input.send_keys(login)
        login_input.send_keys(Keys.TAB)
        time.sleep(1)
        print("✅ Логин введён")

        # Поле для ввода пароля
        password_input = self.driver.find_element(
            By.XPATH, "//input[@type='password']"
        )
        password_input.clear()
        password_input.send_keys(password)
        time.sleep(1)
        print("✅ Пароль введён")

        # Кнопка "Войти"
        try:
            login_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//div[contains(text(), 'Войти')]")
                )
            )
        except Exception:
            login_button = self.wait.until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[contains(text(), 'Войти')]")
                )
            )

        # Прокрутка к кнопке
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});", login_button
        )
        time.sleep(1)

        # Клик через ActionChains
        try:
            actions = ActionChains(self.driver)
            actions.move_to_element(login_button).click().perform()
            print("✅ Кнопка 'Войти' нажата через ActionChains")
        except Exception:
            self.driver.execute_script("arguments[0].click();", login_button)
            print("✅ Кнопка 'Войти' нажата через JavaScript")

        time.sleep(5)
        return MainPage(self.driver)
