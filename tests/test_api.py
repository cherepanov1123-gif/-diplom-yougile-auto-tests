"""
Модуль с API-тестами для YouGile.
"""

import allure
import pytest
from api.yougile_api import YougileApi


@allure.epic("API тесты")
@allure.feature("Проекты")
@pytest.mark.api
class TestProjectsApi:
    """
    Класс с API-тестами для работы с проектами.
    """

    @pytest.fixture
    def api(self):
        return YougileApi()

    EXISTING_PROJECT_ID = "3a719de6-43a7-4928-839f-6244009664d6"

    @allure.title("Получение существующего проекта по ID")
    @allure.story("Получение проекта")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_existing_project(self, api):
        response = api.get_project(self.EXISTING_PROJECT_ID)

        assert "id" in response, "В ответе отсутствует id проекта"
        assert response["id"] == self.EXISTING_PROJECT_ID, \
            "ID проекта не совпадает"
        assert "title" in response, "В ответе отсутствует название проекта"

    @allure.title("Создание нового проекта")
    @allure.story("Создание проекта")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_create_project(self, api):
        project_name = "Временный проект"
        response = api.create_project(project_name)

        assert "id" in response, "Проект не был создан"
        project_id = response["id"]

        get_response = api.get_project(project_id)
        assert get_response["id"] == project_id, \
            "Проект не найден после создания"

        api.delete_project(project_id)

    @allure.title("Обновление названия проекта")
    @allure.story("Обновление проекта")
    @allure.severity(allure.severity_level.NORMAL)
    def test_update_project(self, api):
        old_name = "Старое название"
        new_name = "Новое название"

        create_response = api.create_project(old_name)
        project_id = create_response["id"]

        update_response = api.update_project(project_id, new_name)
        assert "id" in update_response, "Обновление не подтверждено"

        get_response = api.get_project(project_id)
        assert get_response["title"] == new_name, \
            "Название не обновилось"

        api.delete_project(project_id)

    @allure.title("Получение списка всех проектов")
    @allure.story("Получение списка проектов")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_projects_list(self, api):
        response = api.get_projects()

        assert "content" in response, "В ответе нет поля content"
        assert isinstance(response["content"], list), \
            "content не является списком"
        assert len(response["content"]) > 0, "Список проектов пуст"

    @allure.title("Создание проекта с пустым названием")
    @allure.story("Создание проекта")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_project_empty_title(self, api):
        response = api.create_project("")

        assert "error" in response, "В ответе нет поля error"
        assert response.get("statusCode") == 400, \
            "Неверный статус-код"

    @allure.title("Получение несуществующего проекта")
    @allure.story("Получение проекта")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_nonexistent_project(self, api):
        fake_id = "99999999-9999-9999-9999-999999999999"
        response = api.get_project(fake_id)

        assert response.get("statusCode") == 404, \
            "Неверный статус-код"
        assert "error" in response, "В ответе нет поля error"
