
## Описание проекта

Проект создан для автоматизации тестирования трёх ключевых функций YouGile:
- **Создание проекта**
- **Создание доски**
- **Создание колонки**

В проекте реализованы:
- **6 API-тестов** (позитивные и негативные сценарии)
- **5 UI-тестов** (с использованием Page Object Model)
- **Allure-отчёты** для визуализации результатов

---

## Структура проекта

- `api/` — классы для работы с API YouGile
- `pages/` — Page Object'ы для UI-тестов
- `tests/` — тесты (API + UI)
- `config/` — настройки и переменные окружения
- `allure-results/` — сырые данные для Allure-отчёта
- `allure-report/` — сгенерированный HTML-отчёт Allure

---

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone https://github.com/cherepanov1123-gif/-diplom-yougile-auto-tests.git
cd -diplom-yougile-auto-tests
2. Установить зависимости
bash
pip install -r requirements.txt
3. Создать файл .env с переменными
Создай в корне проекта файл .env и добавь в него:

env
BASE_URL=https://yougile.com/api-v2
API_KEY=ваш_ключ
COMPANY_ID=ваш_company_id
LOGIN=ваш_логин
PASSWORD=ваш_пароль
4. Запустить тесты
bash
# Все тесты
pytest

# Только API-тесты
pytest -m api

# Только UI-тесты
pytest -m ui
Allure-отчёт
1. Запустить тесты с сохранением результатов
bash
pytest --alluredir=allure-results
2. Сгенерировать HTML-отчёт
bash
allure generate allure-results -o allure-report
3. Открыть отчёт в браузере
bash
allure open allure-report
Ссылка на финальный проект по ручному тестированию
Тест-план YouGile

Контакты
Автор: Черепанов Александр

Email: cherepanov1123@gmail.com

GitHub: cherepanov1123-gif

© 2026 Черепанов Александр. Дипломная работа по автоматизации тестирования.
