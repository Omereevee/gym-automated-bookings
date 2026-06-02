import os
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ---- sets email and password ---- #
EMAIL = "iamcravingagummybear@test.com"
PASSWORD = "Zaid@12?"

# ---- keeps browzer open ---- #
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# ---- creates a file in local that stores user info ---- #
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

# ---- added stability arguments to prevent profile crashes ---- #
chrome_options.add_argument("--remote-allow-origins=*")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

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
email.send_keys(EMAIL, Keys.ENTER)
password.send_keys(PASSWORD)
sign_in_button = driver.find_element(By.ID, "submit-button")
sign_in_button.click()

time.sleep(5)

# ---- finds the next thursday date ---- #
today = datetime.date.today()
days_ahead = (3 - today.weekday()) % 7
if days_ahead == 0:
    days_ahead = 7

next_thursday = today + datetime.timedelta(days=days_ahead)
thursday_month = next_thursday.strftime("%b").lower()
thursday_day = next_thursday.day

day_container_id = f"day-group-thu-{thursday_month}-{thursday_day}"

# ---- finds thursday tab ---- #
try:
    thursday_tab = driver.find_element(By.CSS_SELECTOR,
                                       f"a[href='#{day_container_id}'], button[data-target='#{day_container_id}'], [id*='thu']")
    thursday_tab.click()
    time.sleep(2)
    # ---- finds the 6:00 events in thurday ---- #
    book_button = driver.find_element(By.CSS_SELECTOR, "button[id$='2026-06-04-1800']")
    # ---- books it ---- #
    driver.execute_script("arguments[0].click();", book_button)
    print("Successfully clicked the 6:00 PM Book Class button!")
except Exception as e:
    # ---- if no 6:00 events on thursday ---- #
    print("Could not find a 6:00 PM class button for this Thursday.", e)


my_bookings = driver.find_element(By.ID, "my-bookings-link")
my_bookings.click()
