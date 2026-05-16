from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Click Vote without selecting option
vote_button = wait.until(
    EC.element_to_be_clickable((By.ID, "vote-poll-1"))
)

vote_button.click()

print("Vote button clicked")

input("Press Enter to close browser...")

driver.quit()