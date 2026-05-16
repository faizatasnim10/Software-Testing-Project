from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Create Chrome driver
driver = webdriver.Chrome()

# Open website
driver.get("https://demowebshop.tricentis.com")

# Maximize browser
driver.maximize_window()

# Create explicit wait
wait = WebDriverWait(driver, 10)

# Click on Books header
books_link = wait.until(
    EC.element_to_be_clickable((By.LINK_TEXT, "Books"))
)

books_link.click()

print("Books page opened")

# Wait for Sort By dropdown
sort_dropdown = wait.until(
    EC.presence_of_element_located((By.ID, "products-orderby"))
)

# Create Select object
dropdown = Select(sort_dropdown)

# Select "Price: Low to High"
dropdown.select_by_visible_text("Price: Low to High")

print("Selected: Price: Low to High")

# Keep browser open
input("Press Enter to close browser...")

# Close browser
driver.quit()