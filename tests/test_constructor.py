from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By
import pytest

#Проверка перехода на вкладку "Консруктор" из личного кабинета
class TestConstructor:
    def test_constructor(self, driver, login_home_page):
        assert login_home_page == True
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.CONSTRUCTOR).click()        
             
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//*[text() = 'Оформить заказ']")))        
        driver.quit() 
#Проверка перехода на вкладку "Консруктор" через логотип Stellar Burgers из личного кабинета
    def test_logo(self, driver, login_home_page):
        assert login_home_page == True
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()         
        driver.find_element(*Locators.LOGO).click()              
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//*[text() = 'Оформить заказ']")))
        driver.quit() 
