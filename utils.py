from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions
from typing import Optional

TIMEOUT_IN_SECONDS = 30
MAGALU_WEBSITE_URL = "https://www.magazineluiza.com.br/"


def init_web_driver(arguments: list[str]):
    webdriver_options = webdriver.ChromeOptions()

    for argument in arguments:
        webdriver_options.add_argument(argument)

    browser = webdriver.Chrome(options=webdriver_options)
    waiter = WebDriverWait(browser, TIMEOUT_IN_SECONDS)

    return browser, waiter

def handle_page_access(browser: Chrome, waiter: WebDriverWait):
    browser.get(MAGALU_WEBSITE_URL)
    
    waiter.until(expected_conditions.url_to_be(MAGALU_WEBSITE_URL))
    assert "Magazine" in browser.title

    print("Magazine Luiza accessed successfully")
    
    
def test_case_success(test_name: str):
    print(f"\033[92m{test_name}: SUCCESS \033[00m")
    
def test_case_failure(test_name: str, message: str, e: Optional[Exception] = None):
    if e is not None:  
        print(f"\033[91m {test_name}: FAILURE - {message} \033[00m", e)
    else:
        print(f"\033[91m {test_name}: FAILURE - {message} \033[00m]")
    