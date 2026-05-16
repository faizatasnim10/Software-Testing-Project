from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Chrome browser
driver = webdriver.Chrome()

# Open website
driver.get("https://demowebshop.tricentis.com")

# Maximize browser
driver.maximize_window()

# Explicit Wait
wait = WebDriverWait(driver, 10)

# Wait for Login link and click
login_button = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Log in"))
)

login_button.click()

# Wait for Email field
email = wait.until(
    EC.presence_of_element_located((By.ID, "Email"))
)

# Enter Email
email.send_keys("fz.tasnim10@gmail.com")

# Enter Password
driver.find_element(By.ID, "Password").send_keys("123456")

# Click Login button
login_submit = wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, "input.login-button"))
)

login_submit.click()

# Verify successful login
account = wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "account"))
)

print("Login Successful")
print("Logged in user:", account.text)

# Keep browser open
input("Press Enter to close browser...")

# Close browser
driver.quit()