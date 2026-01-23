from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By
import pytest

#Проверка перехода на вкладку "Конструктор" из личного кабинета
class TestConstructor:
    def test_constructor(self, driver, login_home_page):
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()        
        
        reg_text = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CONSTRUCTOR_CHECK)).text 
        assert reg_text == 'Соберите бургер'      
        
        
        
#Проверка перехода на вкладку "Консруктор" через логотип Stellar Burgers из личного кабинета
    def test_logo(self, driver, login_home_page):
        
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()         
        driver.find_element(*Locators.LOGO).click()              
        driver.find_elements(*Locators.CONSTRUCTOR_CHECK)
        
        reg_text = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Locators.CONSTRUCTOR_CHECK)).text 
        assert reg_text == 'Соберите бургер'
        
        