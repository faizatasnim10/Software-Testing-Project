from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create Chrome driver
driver = webdriver.Chrome()

# Open login page
driver.get("https://demowebshop.tricentis.com/login")

# Maximize browser
driver.maximize_window()

# Create explicit wait
wait = WebDriverWait(driver, 10)

# Enter email
email = wait.until(
    EC.presence_of_element_located((By.ID, "Email"))
)

email.send_keys("fz.tasnim10@gmail.com")

# Enter password
password = driver.find_element(By.ID, "Password")

password.send_keys("123456")

# Click login button
login_button = driver.find_element(
    By.CSS_SELECTOR,
    "input.login-button"
)

login_button.click()

print("Login successful")

# Wait for search box
search_box = wait.until(
    EC.presence_of_element_located((By.ID, "small-searchterms"))
)

# Search for Desktop
search_box.send_keys("desktop")

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

print("Search completed successfully")

# Wait for logout button
logout_button = wait.until(
    EC.element_to_be_clickable((By.CLASS_NAME, "ico-logout"))
)

# Click logout
logout_button.click()

print("Logout successful")

# Keep browser open
input("Press Enter to close browser...")

# Close browser
driver.quit()