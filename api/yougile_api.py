"""
Модуль для взаимодействия с API YouGile.
"""

import allure
import requests
from config.config import BASE_URL, API_KEY


class YougileApi:
    """
    Класс для работы с API YouGile.
    """

    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {API_KEY}"
        }

    # ==================== ПРОЕКТЫ ====================

    @allure.step("Создать проект с названием '{name}'")
    def create_project(self, name: str) -> dict:
        """Создаёт новый проект."""
        data = {"title": name}
        response = requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=data
        )
        return response.json()

    @allure.step("Создать проект с названием '{name}' и пользователями")
    def create_project_with_users(self, name: str, users: dict) -> dict:
        """
        Создаёт новый проект с указанными пользователями.

        :param name: Название проекта.
        :param users: Словарь {userId: role}
        :return: Ответ сервера в формате JSON.
        """
        data = {"title": name, "users": users}
        response = requests.post(
            f"{self.base_url}/projects",
            headers=self.headers,
            json=data
        )
        return response.json()

    @allure.step("Получить проект по ID '{project_id}'")
    def get_project(self, project_id: str) -> dict:
        """Получает проект по ID."""
        response = requests.get(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response.json()

    @allure.step("Получить список всех проектов")
    def get_projects(self) -> dict:
        """Получает список всех проектов."""
        response = requests.get(
            f"{self.base_url}/projects",
            headers=self.headers
        )
        return response.json()

    @allure.step("Обновить проект {project_id} на '{new_name}'")
    def update_project(self, project_id: str, new_name: str) -> dict:
        """Обновляет название проекта."""
        data = {"title": new_name}
        response = requests.put(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers,
            json=data
        )
        return response.json()

    @allure.step("Удалить проект {project_id}")
    def delete_project(self, project_id: str) -> dict:
        """Удаляет проект по ID."""
        response = requests.delete(
            f"{self.base_url}/projects/{project_id}",
            headers=self.headers
        )
        return response.json()

    # ==================== ДОСКИ ====================

    @allure.step("Создать доску '{title}' в проекте {project_id}")
    def create_board(self, title: str, project_id: str) -> dict:
        """Создаёт новую доску в проекте."""
        data = {"title": title, "projectId": project_id}
        response = requests.post(
            f"{self.base_url}/boards",
            headers=self.headers,
            json=data
        )
        return response.json()

    @allure.step("Получить доску по ID '{board_id}'")
    def get_board(self, board_id: str) -> dict:
        """Получает доску по ID."""
        response = requests.get(
            f"{self.base_url}/boards/{board_id}",
            headers=self.headers
        )
        return response.json()

    @allure.step("Обновить доску {board_id} на '{title}'")
    def update_board(self, board_id: str, title: str) -> dict:
        """Обновляет название доски."""
        data = {"title": title}
        response = requests.put(
            f"{self.base_url}/boards/{board_id}",
            headers=self.headers,
            json=data
        )
        return response.json()

    @allure.step("Удалить доску {board_id}")
    def delete_board(self, board_id: str) -> dict:
        """Удаляет доску по ID."""
        response = requests.delete(
            f"{self.base_url}/boards/{board_id}",
            headers=self.headers
        )
        return response.json()

    # ==================== КОЛОНКИ ====================

    @allure.step("Создать колонку '{title}' на доске {board_id}")
    def create_column(self, title: str, board_id: str) -> dict:
        """Создаёт новую колонку на доске."""
        data = {"title": title, "boardId": board_id}
        response = requests.post(
            f"{self.base_url}/columns",
            headers=self.headers,
            json=data
        )
        return response.json()

    @allure.step("Получить колонку по ID '{column_id}'")
    def get_column(self, column_id: str) -> dict:
        """Получает колонку по ID."""
        response = requests.get(
            f"{self.base_url}/columns/{column_id}",
            headers=self.headers
        )
        return response.json()

    @allure.step("Обновить колонку {column_id} на '{title}'")
    def update_column(self, column_id: str, title: str) -> dict:
        """Обновляет название колонки."""
        data = {"title": title}
        response = requests.put(
            f"{self.base_url}/columns/{column_id}",
            headers=self.headers,
            json=data
        )
        return response.json()

    @allure.step("Удалить колонку {column_id}")
    def delete_column(self, column_id: str) -> dict:
        """Удаляет колонку по ID."""
        response = requests.delete(
            f"{self.base_url}/columns/{column_id}",
            headers=self.headers
        )
        return response.json()
