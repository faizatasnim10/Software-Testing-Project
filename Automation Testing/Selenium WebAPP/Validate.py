from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Click Vote button without selecting answer
vote_button = wait.until(
    EC.element_to_be_clickable((By.ID, "vote-poll-1"))
)

vote_button.click()

# Wait for alert
alert = wait.until(EC.alert_is_present())

# Print alert message
print("Alert Message:", alert.text)

# Validation
assert "Please select an answer" in alert.text

print("Alert validated successfully")

# Accept alert
alert.accept()

input("Press Enter to close browser...")

driver.quit()