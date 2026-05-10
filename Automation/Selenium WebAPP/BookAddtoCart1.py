from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Create Chrome driver
driver = webdriver.Chrome()

# Open website
driver.get("https://demowebshop.tricentis.com")

# Maximize browser
driver.maximize_window()

# Create explicit wait
wait = WebDriverWait(driver, 10)

# Wait for search box
search_box = wait.until(
    EC.presence_of_element_located((By.ID, "small-searchterms"))
)

# Search for book
search_box.send_keys("book")

# Click search button
search_button = driver.find_element(
    By.CSS_SELECTOR,
    "input.search-box-button"
)

search_button.click()

print("Search completed")

# Wait for products to load
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "product-item"))
)

# Click first Add to Cart button
add_to_cart_button = wait.until(
    EC.element_to_be_clickable((
        By.CSS_SELECTOR,
        "input.button-2.product-box-add-to-cart-button"
    ))
)

add_to_cart_button.click()

print("Book added to cart successfully")

# Wait for success notification
wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, "bar-notification"))
)

print("Add to cart notification displayed")

# Keep browser open
input("Press Enter to close browser...")

# Close browser
driver.quit()