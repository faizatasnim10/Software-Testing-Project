from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Open Chrome browser
driver = webdriver.Chrome()

# Explicit wait
wait = WebDriverWait(driver, 10)

# Open first website
driver.get("https://demowebshop.tricentis.com")

driver.maximize_window()

# Store parent tab
parent_tab = driver.current_window_handle

print("Parent Tab Title:", driver.title)

# Open Amazon in new tab
driver.execute_script("window.open('https://demowebshop.tricentis.com/books');")

# Open Google in another tab
driver.execute_script("window.open('https://demowebshop.tricentis.com/login');")

# Wait until 3 tabs are opened
wait.until(EC.number_of_windows_to_be(3))

# Get all tabs
tabs = driver.window_handles

# Switch to Amazon tab
driver.switch_to.window(tabs[1])

print("\nSwitched to Amazon Tab")
print("Title:", driver.title)

time.sleep(2)

# Switch to Google tab
driver.switch_to.window(tabs[2])

print("\nSwitched to Google Tab")
print("Title:", driver.title)

time.sleep(2)

# Switch back to Demo Web Shop
driver.switch_to.window(parent_tab)

print("\nSwitched Back to Demo Web Shop")
print("Title:", driver.title)

# Keep browser open
input("\nPress Enter to close browser...")

# Close browser
driver.quit()