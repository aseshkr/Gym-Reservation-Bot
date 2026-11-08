
# ==========================================
# GYM RESERVATION BOT
# Python + Selenium + Google Chrome
# ==========================================

# Section 1: Import libraries

import os
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from selenium.common.exceptions import TimeoutException


# Section 2: Load environment variables

load_dotenv()

website = os.getenv("GYM_BOOKING_URL")
gym_username = os.getenv("GYM_USERNAME")
gym_password = os.getenv("GYM_PASSWORD")
booking_date = os.getenv("BOOKING_DATE")
time_slot = os.getenv("TIME_SLOT_TEXT")


# Section 3: Validate configuration

if not all([website, gym_username, gym_password,
            booking_date, time_slot]):
    raise ValueError("Missing environment variables in .env file")

print("Environment variables loaded successfully!")


# Section 4: Start Chrome browser

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)

try:

    # Open gym website
    driver.get(website)

    print("Website opened:", driver.title)

    # Section 5: Login automation

    username_field = wait.until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    password_field = driver.find_element(
        By.NAME, "password"
    )

    username_field.send_keys(gym_username)
    password_field.send_keys(gym_password)

    driver.find_element(
        By.CSS_SELECTOR, "button[type='submit']"
    ).click()

    print("Login successful!")

    # Section 6: Select booking date

    date_field = wait.until(
        EC.presence_of_element_located((By.NAME, "date"))
    )

    date_field.send_keys(booking_date)

    # Section 7: Select time slot

    time_dropdown = Select(
        driver.find_element(By.NAME, "timeSlot")
    )

    time_dropdown.select_by_visible_text(time_slot)

    print("Date and time selected successfully!")

    # Section 8: Book gym slot

    book_button = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "button.book")
        )
    )

    book_button.click()

    # Section 9: Verify booking confirmation

    confirmation = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, ".booking-confirmation")
        )
    )

    print("Booking result:", confirmation.text)

    # Section 10: Save screenshot

    driver.save_screenshot("booking_confirmation.png")

    print("Screenshot saved successfully!")
    print("Gym Reservation Bot completed successfully!")

except TimeoutException:

    print("Error: A required website element was not found.")

    driver.save_screenshot("booking_error.png")

except Exception as error:

    print("An unexpected error occurred:", error)

    driver.save_screenshot("booking_error.png")

finally:

    # Always close Chrome
    driver.quit()

    print("Browser closed.")
