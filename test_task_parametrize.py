import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="module")
def result_message():
    result_message = []
    yield result_message
    print(''.join(result_message))

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(7)
    yield browser

    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_get_response_message(browser, number, result_message):
    
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    
    input = browser.find_element(By.CSS_SELECTOR, value = "textarea.ember-text-area.ember-view.textarea.string-quiz__textarea")
    answer = math.log(int(time.time()))
    input.send_keys(answer)
    
    wait = WebDriverWait(browser, 10)
    button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.submit-submission")))
    button.click()

    feedback = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
    feedback_text = feedback.text

    if feedback_text != "Correct!":
        result_message.append(feedback_text)

    assert feedback_text == "Correct!", "Answer is incorrect"





