'''
Requirements:
selenium
webdriver_manager

To build:
pipenv is used
install all the requirements in a pipenv environment
install pyinstaller
run the following command:
pyinstaller --clean .\monkettypebot.spec
'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time

from webdriver_manager.chrome import ChromeDriverManager

# params
opt = True
delay = 0.06
delayRan = 0.05
div = 3
diva = 2
algo = 2

options = webdriver.ChromeOptions()
if opt:
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

driver.get('https://monkeytype.com/')

def monkeytype():
    try:
        driver.find_elements(By.CLASS_NAME, "acceptAll")[0].click()
    except Exception as e:
        print("")

    if algo == 0:
        try:
            while len(driver.find_elements(By.CLASS_NAME, "word")) != 0:
                ActionChains(driver).send_keys([letter.text for letter in driver.find_element(By.CSS_SELECTOR, ".word.active").find_elements(By.TAG_NAME, "letter")] + [' ']).perform()
                time.sleep(delay)
        except Exception as e:
            print("")
    
    elif algo == 1:
        try:
            count = 0
            while len(driver.find_elements(By.CLASS_NAME, "word")) != 0:
                delayE = delay
                cc = count % div
                if cc <= diva:
                    delayE += delayRan * cc
                elif cc > diva:
                    delayE -= 0.5 * delayRan
                active_word = driver.find_element(By.CSS_SELECTOR, ".word.active")
                letters = [letter.text for letter in active_word.find_elements(By.TAG_NAME, "letter")] + [' ']
                for letter in letters:
                    ActionChains(driver).send_keys(letter).perform()
                    time.sleep(delay)
                    count += 1
                
        except Exception as e:
            print(e)
            
    elif algo == 2:
        try:
            while True:
                count = 0
                while len(driver.find_elements(By.CLASS_NAME, "word")) != 0:
                    delayE = delay
                    cc = count % div
                    if cc <= diva:
                        delayE += delayRan * cc
                    elif cc > diva:
                        delayE -= 0.5 * delayRan
                    active_word = driver.find_element(By.CSS_SELECTOR, ".word.active")
                    letters = [letter.text for letter in active_word.find_elements(By.TAG_NAME, "letter")] + [' ']
                    for letter in letters:
                        ActionChains(driver).send_keys(letter).perform()
                        time.sleep(delay)
                        count += 1
                
                time.sleep(5)
                
                ActionChains(driver).send_keys(Keys.TAB).perform()
                
                time.sleep(2)
            
        except Exception as e:
            print(e)
    

input("Press any KEY to Start--")

monkeytype()

input("Ended--")

driver.close()