from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Start Chrome browser
driver = webdriver.Chrome()

# 2. Open Google
driver.get("https://www.google.com")

# 3. Wait for page to load
time.sleep(2)

# 4. Find the Google search box
search_box = driver.find_element(By.NAME, "q")

# 5. Type something
search_box.send_keys("Selenium Python")

# 6. Press ENTER
search_box.send_keys(Keys.RETURN)

# 7. Wait to see results
time.sleep(5)

# 8. Close browser
driver.quit()
