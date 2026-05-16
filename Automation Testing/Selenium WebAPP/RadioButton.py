from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Select radio button
radio_button = wait.until(
    EC.element_to_be_clickable((By.ID, "pollanswers-2"))
)

radio_button.click()

print("Radio button selected")

input("Press Enter to close browser...")

driver.quit()