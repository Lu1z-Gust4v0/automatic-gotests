from utils import init_web_driver, handle_page_access,test_case_failure, test_case_success

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

SEARCH_INPUT_SELECTOR = "input[data-testid='input-search']"
SEARCH_BUTTON_SELECTOR = "svg[data-testid='search-submit']"
ITEM_SEARCH_FILTER_XPATH = "//p[@data-testid='filter-item-text' and contains(text(), '220V')]"
FIRST_PRODUCT_SELECTOR = "ul li a[data-testid='product-card-container']"
PRODUCT_ATTRIBUTE_XPATH = "//label[@data-testid='attribute-item' and contains(text(), '220V')]"
PURCHASE_PRODUCT_BUTTON_SELECTOR = "button[data-testid='buyButton']"

DEFAULT_ERROR_MESSAGE = "An error happened"

def should_make_a_successful_item_search_when_clicking_search_button():
    try: 
        browser, waiter = init_web_driver(['--start-maximized'])  
        
        handle_page_access(browser, waiter)
        
        # Make sure the search input is available
        waiter.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, SEARCH_INPUT_SELECTOR)
            )
        )
        
        search_input = browser.find_element(By.CSS_SELECTOR, SEARCH_INPUT_SELECTOR)
        search_input.send_keys("Geladeira")
        
        search_button = browser.find_element(By.CSS_SELECTOR, SEARCH_BUTTON_SELECTOR) 
        search_button.click()
        
        time.sleep(5)
        
        test_case_success("should_make_a_successful_item_search_when_clicking_search_button")
        
        browser.close()
        
    except Exception as e: 
        test_case_failure("should_make_a_successful_item_search_when_clicking_search_button", DEFAULT_ERROR_MESSAGE, e)
        browser.close()
    
    
def should_make_a_successful_item_search_when_pressing_enter():
    try: 
        browser, waiter = init_web_driver(['--start-maximized'])  
        
        handle_page_access(browser, waiter)
        
        # Make sure the search input is available
        waiter.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, SEARCH_INPUT_SELECTOR)
            )
        )
        
        search_input = browser.find_element(By.CSS_SELECTOR, SEARCH_INPUT_SELECTOR)
        search_input.send_keys("Geladeira")
        
        search_input.send_keys(Keys.ENTER)
        
        time.sleep(5)
        
        test_case_success("should_make_a_successful_item_search_when_pressing_enter")
        
        browser.close()
        
    except Exception as e: 
        test_case_failure("should_make_a_successful_item_search_when_pressing_enter", DEFAULT_ERROR_MESSAGE, e)
        browser.close()
        

def should_successfully_apply_a_filter_in_item_search():
    try: 
        browser, waiter = init_web_driver(['--start-maximized'])  
        
        handle_page_access(browser, waiter)
        
        # Make sure the search input is available
        waiter.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, SEARCH_INPUT_SELECTOR)
            )
        )
        
        search_input = browser.find_element(By.CSS_SELECTOR, SEARCH_INPUT_SELECTOR)
        search_input.send_keys("Geladeira")
        
        search_input.send_keys(Keys.ENTER)
        
        waiter.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.XPATH, ITEM_SEARCH_FILTER_XPATH)
            )
        )
        
        item_search_filter = browser.find_element(By.XPATH, ITEM_SEARCH_FILTER_XPATH)
        item_search_filter.click()
        
        time.sleep(5)
        
        test_case_success("should_successfully_apply_a_filter_in_item_search")
        
        browser.close()
        
    except Exception as e: 
        test_case_failure("should_successfully_apply_a_filter_in_item_search", DEFAULT_ERROR_MESSAGE, e)
        browser.close()
        
        
def should_successfully_click_purchase_button_in_item_card():
    try: 
        browser, waiter = init_web_driver(['--start-maximized'])  
        
        handle_page_access(browser, waiter)
        
        # Make sure the search input is available
        waiter.until(
            expected_conditions.visibility_of_element_located(
                (By.CSS_SELECTOR, SEARCH_INPUT_SELECTOR)
            )
        )
        
        search_input = browser.find_element(By.CSS_SELECTOR, SEARCH_INPUT_SELECTOR)
        search_input.send_keys("Geladeira")
        
        search_input.send_keys(Keys.ENTER)
        
        waiter.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.XPATH, ITEM_SEARCH_FILTER_XPATH)
            )
        )
        
        item_search_filter = browser.find_element(By.XPATH, ITEM_SEARCH_FILTER_XPATH)
        item_search_filter.click()
        
        waiter.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, FIRST_PRODUCT_SELECTOR)
            )
        )
        
        first_product = browser.find_element(By.CSS_SELECTOR, FIRST_PRODUCT_SELECTOR)
        first_product.click()
        
        time.sleep(5)
        
        product_attribute = browser.find_element(By.XPATH, PRODUCT_ATTRIBUTE_XPATH)
        
        if product_attribute:
            product_attribute.click()
        
        waiter.until(
            expected_conditions.visibility_of_all_elements_located(
                (By.CSS_SELECTOR, PURCHASE_PRODUCT_BUTTON_SELECTOR)
            )
        )
        
        purchase_button = browser.find_element(By.CSS_SELECTOR, PURCHASE_PRODUCT_BUTTON_SELECTOR)
        purchase_button.click()
        
        time.sleep(5)
        
        test_case_success("should_successfully_click_purchase_button_in_item_card")
        
        browser.close()
        
    except Exception as e: 
        test_case_failure("should_successfully_click_purchase_button_in_item_card", DEFAULT_ERROR_MESSAGE, e)
        browser.close()
    
    
def main():
    should_make_a_successful_item_search_when_clicking_search_button()
    should_make_a_successful_item_search_when_pressing_enter()
    should_successfully_apply_a_filter_in_item_search()
    should_successfully_click_purchase_button_in_item_card()
    
if __name__ == "__main__":
    main()