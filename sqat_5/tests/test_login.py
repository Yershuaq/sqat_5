import logging
from selenium.webdriver.common.by import By

def test_login_positive(driver):
    """
    Expected: User is redirected to Dashboard.
    Actual: Check if 'Dashboard' header is visible.
    """
    logging.info("Шаг 1: Переход на страницу логина")
    driver.get("https://opensource-demo.orangehrmlive.com/")
    
    logging.info("Шаг 2: Ввод Admin / admin123")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.TAG_NAME, "button").click()
    
    # Анализ результата
    header = driver.find_element(By.TAG_NAME, "h6").text
    logging.info(f"Анализ: Ожидаем 'Dashboard', получили '{header}'")
    assert header == "Dashboard", f"Ошибка! Ожидалось 'Dashboard', но получили '{header}'"