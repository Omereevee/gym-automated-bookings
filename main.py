import os
import time
import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# ---- sets email and password ---- #
EMAIL = "iamcravingagummybear@test.com"
PASSWORD = "Zaid@12?"

# ---- keeps browser open ---- #
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


next_thursday = today + datetime.timedelta(days=days_ahead)
thursday_month = next_thursday.strftime("%b").lower()
thursday_day = next_thursday.day

if thursday_day < 10:
    thursday_day_format = f"0{thursday_day}"
else:
    thursday_day_format = thursday_day


thursday_month_format = datetime.datetime.strptime(thursday_month, "%b").strftime("%m")
day_container_id = f"day-group-thu-{thursday_month}-{thursday_day}"

# ---- finds thursday tab ---- #

booked = 0
waitlisted = 0
already_booked = 0

try:
    thursday_tab = driver.find_element(By.CSS_SELECTOR,
                                       f"a[href='#{day_container_id}'], button[data-target='#{day_container_id}'], [id*='thu']")

    thursday_tab.click()
    time.sleep(2)

    # ---- finds the 6:00 events in thurday ---- #
    book_button = driver.find_element(By.CSS_SELECTOR, f"button[id$='2026-{thursday_month_format}-{thursday_day_format}-1800']")

    # ---- books it ---- #
    if  book_button.text == "Booked":
        print(f"Already booked: Spin Class on Thursday, {thursday_month}, {thursday_day}")
        already_booked += 1


    elif book_button.text == "Waitlisted":
        print(f"Already on waitlist: Spin Class on Thursday, {thursday_month}, {thursday_day}")
        already_booked += 1

    elif book_button.text == "Join Waitlist":
        driver.execute_script("arguments[0].click();", book_button)
        print(f"Joined waitlist for: Spin Class on Thursday, {thursday_month}, {thursday_day}")
        waitlisted += 1

    elif  book_button.text == "Book Class":
        driver.execute_script("arguments[0].click();", book_button)
        print(f"Joined waitlist for: Spin Class on Thursday, {thursday_month}, {thursday_day}")
        booked += 1

    # ---- if no 6:00 events on thursday ---- #
except Exception as e:
    print(f"Could not find a 6:00 PM class button for {thursday_month} : {thursday_day}.", e)



my_bookings = driver.find_element(By.ID, "my-bookings-link")
my_bookings.click()

# ---- SUMMARY ---- #

print(f"--- BOOKING SUMMARY ---\nClasses booked: {booked}\nWaitlists joined: {waitlisted}\nAlready booked/waitlisted: {already_booked}\nTotal Tuesday 6pm classes processed: {already_booked + booked + waitlisted}")



