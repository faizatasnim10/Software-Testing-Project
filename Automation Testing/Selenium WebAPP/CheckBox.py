from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com/login")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Locate checkbox
checkbox = wait.until(
    EC.element_to_be_clickable((By.ID, "RememberMe"))
)

# Click checkbox
checkbox.click()

# Validate checkbox selected
if checkbox.is_selected():
    print("Checkbox is selected")
else:
    print("Checkbox is NOT selected")

input("Press Enter to close browser...")

driver.quit()