STALL_AFTER_LOGIN = 6

NUMBER_OF_DAYS = 14

EARLIEST_TIME = "12:16pm"

LATEST_TIME = "12:44am"

LONGEST_SHIFT = 8

WEEKDAYS = [
"Monday",
"Tuesday",
"Wednesday",
"Thursday",
"Friday",
"Saturday",
"Sunday"
]


CHROME_PROFILE_DIRECTORY_PATH = r"Chrome user profile directory goes here"

LOGIN_URL = "https://atoz.amazon.work"

USERNAME = "AtoZ username goes here"

PASSWORD = "AtoZ password goes here"

HOURS_TO_RUN = 3  # Hours

SECONDS_BETWEEN_CHECKS = 30

import time
import undetected_chromedriver as uc
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options as ChromeOptions

class Browser:

    def __init__(self):
        self.options = ChromeOptions()
        self.options.add_argument(f"--user-data-dir={CHROME_PROFILE_DIRECTORY_PATH}")
        self.driver = uc.Chrome(options=self.options)
        self.driver.get("https://atoz.amazon.work")

    def login(self):
        uname = self.driver.find_element(By.XPATH, "//input[@id='login']")
        uname.send_keys(USERNAME)
        pword = self.driver.find_element(By.XPATH, "//input[@id='password']")
        pword.send_keys(PASSWORD)
        submit = self.driver.find_element(By.XPATH, "//button[@id='buttonLogin']")
        submit.click()
        time.sleep(STALL_AFTER_LOGIN)

    def authenticate(self):
        element = self.driver.find_element(By.XPATH, "//input[@value='1']")
        element.click()
        button = self.driver.find_element(By.XPATH, "//button[@id='buttonContinue']")
        button.click()
        time.sleep(4)


    def stall_until_solved(self):
        while True:
            try:
                header = self.driver.find_element(By.XPATH, "//h1[@class='top-h1']")
                if "Verify your identity" in header.text:
                    self.driver.find_element(By.XPATH, "//input[@id='code']")
                    time.sleep(10)
            except:
                break

    def check_verify(self):
        try:
            self.authenticate()
            checkbox = self.driver.find_element(By.XPATH, "//label[@id='trusted-device-option-label']")
            checkbox.click()
            self.stall_until_solved()
        except:
            pass

    def save_cookies(self):
        cookies = self.driver.get_cookies()
        json.dump(cookies, open("cookies", "wt", encoding="utf8"))

    def exit(self):
        self.driver.quit()


    def back_home(self):
        link = self.driver.find_element(By.XPATH, "//ul[contains(@class, 'navbar-left')]/li[@class='active']/a")
        link.click()


    def find_shifts(self):
        button = self.driver.find_element(By.XPATH, "//button[@data-testid='FindShiftsQuickLink']")
        button.click()
        time.sleep(2)
        for i, element in enumerate(self.driver.find_elements(By.XPATH, "//div[@data-test-id='day-card']")):
            if i > NUMBER_OF_DAYS:
                break
            element.click()
            for row in self.driver.find_elements(By.XPATH, "//div[@role='listitem']"):
                try:
                    add_shift = row.find_element(By.XPATH, ".//button[@aria-label='Add shift button']")
                    # view_details = row.find_element(By.XPATH, ".//button[@aria-label='View details button']")
                    textelem = row.find_element(By.XPATH, ".//div[@data-test-component='StencilText']")
                    hours = textelem.text
                    parts = hours.split(" ")
                    start, end = parts[0].split("-")
                    first = parse_hour(start)
                    earlier_time = parse_hour(EARLIEST_TIME)
                    later_time = parse_hour(LATEST_TIME)
                    if first >= earlier_time and first <= later_time:
                        shift_end = parse_hour(end)
                        if time_diff(shift_end, first) <= LONGEST_SHIFT:
                            day = element.find_element(By.XPATH, "./div/div").text
                            if day in WEEKDAYS:
                                # view_details.click()
                                add_shift.click()
                                time.sleep(2)
                                button = self.driver.find_element(By.XPATH, "//button[@data-test-id='AddOpportunityModalSuccessDoneButton']")
                                button.click()
                except Exception as ex:
                    pass

def parse_hour(hora):
    hour, mint = hora.split(":")
    minute = "".join([i for i in mint if i.isdigit()])
    section = mint[len(minute):]
    hour, minute = int(hour), int(minute)
    if section == "pm" and hour != 12:
        hour += 12
    return (hour, minute)

def earlier_time(time1, time2):
    if time1[0] > time2[0]:
        return time2
    elif time1[0] < time2[0]:
        return time1
    elif time1[1] > time2[1]:
        return time2
    else:
        return time1

def time_diff(time1, time2):
    if time1[0] < time2[0]:
        midnight_offset = 24 - time2[0]
        time2 = list(time2)
        time2[0] = - midnight_offset
    diff = time1[0] - time2[0]
    diff -= time1[1] / 60
    diff += time2[1] / 60
    return diff

def main():
    start = time.time()
    browser = Browser()
    browser.login()
    browser.check_verify()
    browser.save_cookies()
    while time.time() - start < HOURS_TO_RUN * 60 * 60:
        browser.find_shifts()
        browser.back_home()
        done = time.time()
        while time.time() - done < SECONDS_BETWEEN_CHECKS:
            time.sleep(5)
    browser.exit()

if __name__ == "__main__":
    main()
