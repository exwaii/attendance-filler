from dotenv import load_dotenv
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from formfiller import finalform


load_dotenv()

driver_path = os.getenv("DRIVER_PATH")
email = os.getenv("EDU_EMAIL")
username = os.getenv("DET_USERNAME")
password = os.getenv("DET_PASSWORD")


def submit(form):
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(
        executable_path=driver_path, options=chrome_options)

    # login to edu email acc

    url = 'https://accounts.google.com/Login'
    driver.get(url)

    print(driver.title)
    ActionChains(driver).send_keys(email).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    sleep(5)

    # det login

    ActionChains(driver).send_keys(username).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(password).perform()
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    sleep(1)
    ActionChains(driver).send_keys(Keys.ENTER).perform()
    sleep(1)

    # uncomment for not headless mode
    continue_span = driver.find_element(By.XPATH, '//span[text()="Continue"]')
    continue_span.click()

    sleep(5)

    # open prefilled form

    driver.get(form)
    sleep(1)

    # confirm email submission in forms

    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.TAB).perform()
    ActionChains(driver).send_keys(Keys.SPACE).perform()

    for i in range(3):
        next_span = driver.find_element(By.XPATH, '//span[text()="Next"]')
        next_span.click()
        sleep(1)

    submit_span = driver.find_element(By.XPATH, '//span[text()="Submit"]')
    submit_span.click()
    sleep(2)

    # Close the browser window
    driver.quit()


def main():
    submit(finalform(1))


if __name__ == "__main__":
    main()

