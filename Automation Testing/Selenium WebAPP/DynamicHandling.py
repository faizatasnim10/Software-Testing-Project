from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://demowebshop.tricentis.com")

driver.maximize_window()

wait = WebDriverWait(driver, 10)

# Locate search box
search_box = wait.until(
    EC.presence_of_element_located((By.ID, "small-searchterms"))
)

# Search for product
search_box.send_keys("book")

# Click search button
driver.find_element(By.CSS_SELECTOR, "input.search-box-button").click()

# Wait for products to load
products = wait.until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h2.product-title"))
)

print("Search Results Found:")

# Print all dynamic products
for product in products:
    print(product.text)

input("Press Enter to close browser...")

driver.quit()