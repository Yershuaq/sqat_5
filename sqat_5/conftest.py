import pytest
import logging
import os
import time
from selenium import webdriver
from datetime import datetime


if not os.path.exists("logs"):
    os.makedirs("logs")

logging.basicConfig(
    filename="logs/automation.log",  
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    force=True
)


@pytest.fixture(scope="function")
def driver(request):
    logging.info(f"--- СТАРТ ТЕСТА: {request.node.name} ---")
    
    driver = webdriver.Chrome() 
    driver.implicitly_wait(10)
    driver.maximize_window()
    
    yield driver  
    

    time.sleep(2) 
    
    if not os.path.exists("reports/screenshots"):
        os.makedirs("reports/screenshots")
    
    screenshot_name = f"{request.node.name}.png"
    screenshot_path = os.path.join("reports/screenshots", screenshot_name)
    driver.save_screenshot(screenshot_path)
    logging.info(f"Скриншот сохранен: {screenshot_path}")

    logging.info(f"--- ЗАВЕРШЕНИЕ ТЕСТА: {request.node.name} ---")
    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call':
        screenshot_path = f"screenshots/{item.name}.png"
        
        if pytest_html is not None:
            extra.append(pytest_html.extras.image(screenshot_path))
            report.extra = extra
            
        if report.failed:

            logging.error(f"ТЕСТ ПРОВАЛЕН: {item.nodeid}. Ошибка: {report.longreprtext}")
