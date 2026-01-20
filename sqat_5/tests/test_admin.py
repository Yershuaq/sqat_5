import logging
from selenium.webdriver.common.by import By

def test_admin_search_user(driver):
    """
    Expected: System filters and shows 'Admin' user in the table.
    """
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.TAG_NAME, "button").click()

    logging.info("Шаг: Поиск пользователя Admin в разделе Admin")
    driver.find_element(By.XPATH, "//span[text()='Admin']").click()
    
    inputs = driver.find_elements(By.CLASS_NAME, "oxd-input")
    inputs[1].send_keys("Admin") # Поле Username
    driver.find_element(By.XPATH, "//button[@type='submit']").click()
    
    # Анализ
    result = driver.find_element(By.XPATH, "//div[contains(text(), 'Admin')]").is_displayed()
    logging.info(f"Анализ: Пользователь найден? {result}")
    assert result == True, "Ошибка: Пользователь Admin не найден в таблице"