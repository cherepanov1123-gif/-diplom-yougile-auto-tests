def pytest_configure(config):
    config.addinivalue_line(
        "markers", "ui: тесты пользовательского интерфейса"
    )
    config.addinivalue_line(
        "markers", "api: тесты API"
    )
