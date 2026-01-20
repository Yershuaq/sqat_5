import pytest
import logging
import os
import time
from selenium import webdriver
from datetime import datetime

# 1. КОНФИГУРАЦИЯ ЛОГИРОВАНИЯ (Требование: 30 pts) [cite: 15]
# Создаем папку для логов, если ее нет
if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/automation.log", # Логи записываются в файл 
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)

# 2. ЖИЗНЕННЫЙ ЦИКЛ ТЕСТА: SETUP И TEARDOWN (Требование: 30 pts) [cite: 9]
@pytest.fixture(scope="function")
def driver(request):
    # Setup: Логируем начало и запускаем браузер [cite: 11, 17]
    logging.info(f"--- СТАРТ ТЕСТА: {request.node.name} ---")
    
    # Инициализация WebDriver
    driver = webdriver.Chrome() 
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver  # Здесь выполняется сам код теста [cite: 14]
    
    # ПЕРЕД ТИРДАУНОМ: Создание скриншота (Требование: 25 pts) [cite: 22, 28]
    # Добавляем паузу 1-2 секунды, чтобы SPA-страница (OrangeHRM) успела отрисоваться
    time.sleep(2) 
    
    if not os.path.exists("reports/screenshots"):
        os.makedirs("reports/screenshots")
    
    # Сохраняем скриншот с именем текущего теста
    screenshot_name = f"{request.node.name}.png"
    screenshot_path = os.path.join("reports/screenshots", screenshot_name)
    driver.save_screenshot(screenshot_path)
    logging.info(f"Скриншот сохранен: {screenshot_path}")

    # Teardown: Логируем конец и закрываем браузер [cite: 12, 17]
    logging.info(f"--- ЗАВЕРШЕНИЕ ТЕСТА: {request.node.name} ---")
    driver.quit()

# 3. ИНТЕГРАЦИЯ В HTML ОТЧЕТ (Требование: Expected vs Actual, Screenshots) [cite: 23, 26, 28]
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Этот хук позволяет добавлять скриншоты и логи прямо в HTML-отчет.
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        # Путь к скриншоту для HTML-отчета (относительно папки reports)
        screenshot_path = f"screenshots/{item.name}.png"
        
        if pytest_html is not None:
            # Прикрепляем скриншот к отчету 
            extra.append(pytest_html.extras.image(screenshot_path))
            report.extra = extra
            
        # Логируем ошибки, если тест провален [cite: 19, 29]
        if report.failed:
            logging.error(f"ТЕСТ ПРОВАЛЕН: {item.nodeid}. Ошибка: {report.longreprtext}")