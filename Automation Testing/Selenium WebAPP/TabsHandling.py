from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Open Demo Web Shop
driver.get("https://demowebshop.tricentis.com")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Store parent window
parent_window = driver.current_window_handle

print("Parent Window Title:", driver.title)

# Open new tab
driver.execute_script("window.open('https://demowebshop.tricentis.com/books');")

# Wait until 2 tabs are opened
wait.until(EC.number_of_windows_to_be(2))

# Get all window handles
all_windows = driver.window_handles

# Switch to second tab
for window in all_windows:
    if window != parent_window:
        driver.switch_to.window(window)
        break

print("Switched To New Tab")
print("Current Title:", driver.title)

time.sleep(3)

# Switch back to parent tab
driver.switch_to.window(parent_window)

print("Back To Parent Tab")
print("Current Title:", driver.title)

input("Press Enter to close browser...")

driver.quit()