from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://practicetestautomation.com/practice-test-login/")

click1 = driver.find_element(By.XPATH,'//input[@id="username"]')
click1.send_keys("student")
time.sleep(2)
click2 = driver.find_element(By.XPATH,'//input[@id="password"]')
click2.send_keys("Password123")
time.sleep(2)

click3 = driver.find_element(By.XPATH, '//button[@id="submit"]')
click3.click()
time.sleep(3)

driver.save_screenshot("login_success.png")
driver.quit()



