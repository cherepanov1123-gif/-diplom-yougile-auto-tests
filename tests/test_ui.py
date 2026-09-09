"""
Модуль с UI-тестами для YouGile.
"""

import time
import allure
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
from pages.main_page import MainPage
from config.config import LOGIN, PASSWORD
from api.yougile_api import YougileApi


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def api():
    return YougileApi()


@allure.title("Авторизация через UI")
@allure.story("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_login_ui(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)

    current_url = driver.current_url
    assert "login" not in current_url, "Авторизация не удалась"
    assert (
        "team" in current_url or
        "dashboard" in current_url or
        "projects" in current_url
    ), "Авторизация не удалась"


@allure.title("Создание проекта через API и проверка в UI")
@allure.story("Проекты")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_project_appears_ui(driver, api):
    project_name = f"UI Проект {int(time.time())}"
    api.create_project(project_name)
    time.sleep(3)

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)

    main_page = MainPage(driver)
    main_page.wait_for_projects_list()

    try:
        main_page.find_project(project_name)
        print(f"✅ Проект '{project_name}' отображается в UI")
    except Exception:
        driver.refresh()
        time.sleep(2)
        main_page.find_project(project_name)

    projects = api.get_projects()
    for p in projects.get("content", []):
        if p.get("title") == project_name:
            api.delete_project(p["id"])
            break


@allure.title("Создание доски через API и проверка в UI")
@allure.story("Доски")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_board_appears_ui(driver, api):
    project_name = f"UI Проект {int(time.time())}"
    project = api.create_project(project_name)
    project_id = project["id"]
    time.sleep(3)

    board_name = f"UI Доска {int(time.time())}"
    api.create_board(board_name, project_id)
    time.sleep(2)

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)

    main_page = MainPage(driver)
    main_page.wait_for_projects_list()

    main_page.find_project(project_name)
    time.sleep(2)

    try:
        driver.find_element(By.XPATH, f"//*[contains(text(), '{board_name}')]")
        print(f"✅ Доска '{board_name}' отображается в UI")
    except Exception:
        driver.refresh()
        time.sleep(2)
        driver.find_element(By.XPATH, f"//*[contains(text(), '{board_name}')]")

    api.delete_project(project_id)


@allure.title("Создание колонки через API и проверка в UI")
@allure.story("Колонки")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.ui
def test_column_appears_ui(driver, api):
    project_name = f"UI Проект {int(time.time())}"
    project = api.create_project(project_name)
    project_id = project["id"]
    time.sleep(3)

    board_name = f"UI Доска {int(time.time())}"
    board = api.create_board(board_name, project_id)
    board_id = board["id"]
    time.sleep(2)

    column_name = f"UI Колонка {int(time.time())}"
    api.create_column(column_name, board_id)

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)

    main_page = MainPage(driver)
    main_page.wait_for_projects_list()

    main_page.find_project(project_name)
    time.sleep(2)

    driver.find_element(
        By.XPATH, f"//*[contains(text(), '{board_name}')]"
    ).click()
    time.sleep(2)

    try:
        driver.find_element(
            By.XPATH, f"//*[contains(text(), '{column_name}')]"
        )
        print(f"✅ Колонка '{column_name}' отображается в UI")
    except Exception:
        driver.refresh()
        time.sleep(2)
        driver.find_element(
            By.XPATH, f"//*[contains(text(), '{column_name}')]"
        )

    api.delete_project(project_id)


@allure.title("Обновление проекта через API и проверка в UI")
@allure.story("Проекты")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.ui
def test_project_update_ui(driver, api):
    old_name = f"UI Проект {int(time.time())}"
    project = api.create_project(old_name)
    project_id = project["id"]
    time.sleep(3)

    new_name = f"UI Проект обновлён {int(time.time())}"

    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(LOGIN, PASSWORD)

    main_page = MainPage(driver)
    main_page.wait_for_projects_list()

    main_page.find_project(old_name)
    print(f"✅ Проект '{old_name}' отображается")

    api.update_project(project_id, new_name)

    driver.refresh()
    time.sleep(3)
    main_page.wait_for_projects_list()
    main_page.find_project(new_name)
    print(f"✅ Проект обновлён на '{new_name}' в UI")

    api.delete_project(project_id)
