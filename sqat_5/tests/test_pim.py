import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_pim_navigation(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/")
    driver.find_element(By.NAME, "username").send_keys("Admin")
    driver.find_element(By.NAME, "password").send_keys("admin123")
    driver.find_element(By.TAG_NAME, "button").click()

    logging.info("Шаг: Клик по меню PIM")
    driver.find_element(By.XPATH, "//span[text()='PIM']").click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h6[text()='PIM']"))
    )
    
    # Анализ
    actual_url = driver.current_url
    logging.info(f"Анализ URL: {actual_url}")

    assert "pim" in actual_url.lower()
