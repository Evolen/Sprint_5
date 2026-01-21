import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import random
from locators import Locators

username = f"testuser{random.randint(10000, 99999)}"
email = f"{username}@yandex.ru" 



@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument("--window-size=1600,900")
    options.add_experimental_option("prefs", {
            "profile.password_manager_leak_detection": False
        })
    #options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    browser.get("https://stellarburgers.education-services.ru/")
    yield browser
    browser.quit()

@pytest.fixture()
def login_registration(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.REG_BUTTON ).click()        
    elements = driver.find_elements(*Locators.NAME)
    elements[0].send_keys(username)
    elements[1].send_keys(email)        
    driver.find_element(*Locators.PASSWORD).send_keys("123456")
    driver.find_element(*Locators.REG_BUTTON_FINALE).click()       
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text() = 'Вход']")))           
    return True


@pytest.fixture()
def login_home_page(driver):
    driver.find_element(*Locators.LOGIN_BUTTON).click()
    driver.find_element(*Locators.EMAIL).send_keys("elengrimm39@yandex.ru") 
    driver.find_element(*Locators.PASSWORD_LOGIN).send_keys("123456")        
    driver.find_element(*Locators.LOGIN_BUTTON_FINALLY).click()      
    return True    
    
@pytest.fixture()
def login_personal_acc(driver):
    driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
    driver.find_element(*Locators.EMAIL).send_keys("elengrimm39@yandex.ru") 
    driver.find_element(*Locators.PASSWORD_LOGIN).send_keys("123456")        
    driver.find_element(*Locators.LOGIN_BUTTON_FINALLY).click()      
    return True 

@pytest.fixture()
def login_pass_recovery(driver):
    driver.find_element(*Locators.LOGIN_BUTTON).click()    
    driver.find_element(*Locators.RECOVERY_PASS).click()        
    driver.find_element(*Locators.RECOVERY_PASS_LOGIN).click()       
    driver.find_element(*Locators.EMAIL).send_keys("elengrimm39@yandex.ru") 
    driver.find_element(*Locators.PASSWORD_LOGIN).send_keys("123456")        
    driver.find_element(*Locators.LOGIN_BUTTON_FINALLY).click()    
    return True 