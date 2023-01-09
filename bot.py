from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

delay = 0.01

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://monkeytype.com/')

def monkeytype():
    try:
        driver.find_elements(By.CLASS_NAME, "acceptAll")[0].click()
    except Exception as e:
        print(e)
        return

    try:
        while len(driver.find_elements(By.CLASS_NAME, "word")) != 0:
            ActionChains(driver).send_keys([letter.text for letter in driver.find_element(By.CSS_SELECTOR, ".word.active").find_elements(By.TAG_NAME, "letter")] + [' ']).perform()
            time.sleep(delay)
    except Exception as e:
        print(e)
    

input("Press any KEY to Start--")

monkeytype()

input("Ended--")

driver.close()