import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.wait import WebDriverWait

# ---- sets email and password ---- #
EMAIL = "iamcravingagummybear@test.com"
PASSWORD = "Zaid@12?"

# ---- keeps browzer open ---- #
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# ---- creates a file in local that stores user info ---- #
user_data_dir = os.path.join(os.getcwd(),"chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# ---- creates driver ---- #
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://appbrewery.github.io/gym/")

# ---- clicks log in button ---- #
log_in_butt = driver.find_element(By.ID, "login-button")
log_in_butt.click()

# ---- finds email and password elements ---- #
time.sleep(2)
email = driver.find_element(By.ID, "email-input")
password = driver.find_element(By.ID, "password-input")

# ---- log in --- #
email.send_keys(EMAIL,Keys.ENTER)
password.send_keys(PASSWORD)
sign_in_button = driver.find_element(By.ID,"submit-button")
sign_in_button.click()

element = WebDriverWait(driver, 20).until(visibility_of_element_located((By.ID, "schedule-page")))
print(element.text)