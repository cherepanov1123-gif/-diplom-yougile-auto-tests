"""
Модуль с классом для главной страницы YouGile.
"""

import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class MainPage(BasePage):
    """
    Класс для главной страницы YouGile.
    """

    @allure.step("Проверить, что главная страница загрузилась")
    def is_loaded(self) -> bool:
        try:
            self.wait.until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".login-title")
                )
            )
            return True
        except Exception:
            return False

    @allure.step("Ожидать загрузку списка проектов")
    def wait_for_projects_list(self):
        self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//*[contains(text(), 'Проекты')]")
            )
        )
        return self

    @allure.step("Нажать на кнопку создания проекта")
    def click_create_project_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Создать проект')]")
            )
        )
        button.click()
        return self

    @allure.step("Ввести название проекта '{name}'")
    def enter_project_name(self, name: str):
        input_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Название проекта']")
            )
        )
        input_field.send_keys(name)
        return self

    @allure.step("Создать проект с названием '{name}'")
    def create_project(self, name: str):
        self.click_create_project_button()
        self.enter_project_name(name)
        create_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Создать')]"
        )
        create_button.click()
        return self

    @allure.step("Найти проект с названием '{name}'")
    def find_project(self, name: str):
        project_locator = (By.XPATH, f"//span[contains(text(), '{name}')]")
        project = self.wait.until(EC.element_to_be_clickable(project_locator))
        project.click()
        return self

    @allure.step("Обновить название проекта на '{new_name}'")
    def update_project_name(self, new_name: str):
        title_locator = (By.XPATH, "//h1[contains(@class, 'project-title')]")
        title = self.wait.until(EC.element_to_be_clickable(title_locator))
        title.click()

        input_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Название проекта']")
            )
        )
        input_field.clear()
        input_field.send_keys(new_name)
        input_field.send_keys("\n")
        return self

    @allure.step("Нажать на кнопку создания доски")
    def click_create_board_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Создать доску')]")
            )
        )
        button.click()
        return self

    @allure.step("Ввести название доски '{name}'")
    def enter_board_name(self, name: str):
        input_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Название доски']")
            )
        )
        input_field.send_keys(name)
        return self

    @allure.step("Создать доску с названием '{name}'")
    def create_board(self, name: str):
        self.click_create_board_button()
        self.enter_board_name(name)
        create_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Создать')]"
        )
        create_button.click()
        return self

    @allure.step("Нажать на кнопку создания колонки")
    def click_create_column_button(self):
        button = self.wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[contains(text(), 'Создать колонку')]")
            )
        )
        button.click()
        return self

    @allure.step("Ввести название колонки '{name}'")
    def enter_column_name(self, name: str):
        input_field = self.wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, "//input[@placeholder='Название колонки']")
            )
        )
        input_field.send_keys(name)
        return self

    @allure.step("Создать колонку с названием '{name}'")
    def create_column(self, name: str):
        self.click_create_column_button()
        self.enter_column_name(name)
        create_button = self.driver.find_element(
            By.XPATH, "//button[contains(text(), 'Создать')]"
        )
        create_button.click()
        return self
