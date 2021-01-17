from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://winners.net/")

try:
    comparison = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Bookmaker Comparison"))
    )
    comparison.click()

    add_bookmaker1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "plus-icon"))
    )
    add_bookmaker1.click()
except:
    driver.quit()

time.sleep(30)
driver.quit()
