from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, пока цена дома уменьшится до $100
WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )

button = browser.find_element_by_id("book")
button.click()

x_element = browser.find_element_by_id('input_value')
x = x_element.text
y = calc(x) 

input = browser.find_element_by_id('answer')
input.send_keys(y)  

button_submit = browser.find_element_by_id("solve")
button_submit.click()

time.sleep(10)
browser.quit()
