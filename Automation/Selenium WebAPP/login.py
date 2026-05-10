from selenium import webdriver
from selenium.webdriver.common.by import By
#import time

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/login")

#time.sleep(2)

driver.find_element(By.ID, "Email").send_keys("fz.tasnim10@gmail.com")
driver.find_element(By.ID, "Password").send_keys("123456")

# click()
driver.find_element(By.CSS_SELECTOR, "input.login-button").click()

# driver.find_element(By.XPATH, "//input[@value='Log in']").click()

#time.sleep(30)

# Keeps browser open
input("Press Enter to close browser...")

driver.quit()






