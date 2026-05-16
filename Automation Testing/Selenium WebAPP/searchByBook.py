from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create Chrome driver
driver = webdriver.Chrome()

# Open website
driver.get("https://demowebshop.tricentis.com")

# Maximize window
driver.maximize_window()

# Create wait
wait = WebDriverWait(driver, 10)

# Wait for search box
search_box = wait.until(
    EC.presence_of_element_located((By.ID, "small-searchterms"))
)

# Enter product name
search_box.send_keys("book")

# Click search button
search_button = driver.find_element(
    By.CSS_SELECTOR,
    "input.search-box-button"
)

search_button.click()

# Wait until redirected to search page
wait.until(
    EC.url_contains("search")
)

# Print current URL
print("Redirected URL:", driver.current_url)

# Assertion to verify redirect
assert "search" in driver.current_url

print("Successfully redirected to search page")

# Keeps browser open
input("Press Enter to close browser...")

driver.quit()