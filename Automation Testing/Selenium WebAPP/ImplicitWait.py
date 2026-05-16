from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

# Implicit wait
driver.implicitly_wait(10)

driver.get("https://demowebshop.tricentis.com")

driver.maximize_window()

# Click Login using LINK_TEXT
driver.find_element(By.LINK_TEXT, "Log in").click()

# Enter Email
driver.find_element(By.ID, "Email").send_keys("fz.tasnim10@gmail.com")

# Enter Password
driver.find_element(By.ID, "Password").send_keys("123456")

# Click Login button
driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

print("Login Successful")

input("Press Enter to close browser...")

driver.quit()