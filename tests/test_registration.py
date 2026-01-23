from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By
import pytest


#Проверка регистрации      
class TestRegistration:
    def test_registration(self, driver,login_registration, ):
        (email, password) = login_registration
        driver.find_element(*Locators.EMAIL).send_keys(email)          
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys(password)        
        driver.find_element(*Locators.LOGIN_BUTTON_FINALLY).click() 
        login_check = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER)).text   
        assert login_check == "Оформить заказ"
              

#Проверка ошибки для неккоректного пароля 
class TestRegistrationFail:
    def test_password_fail(self, driver):

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        driver.find_element(*Locators.REG_BUTTON ).click()        
        elements = driver.find_elements(*Locators.NAME)
        elements[0].send_keys("ELena")
        elements[1].send_keys("grimm39@google.ru")        
        driver.find_element(*Locators.PASSWORD).send_keys("12345")
        driver.find_element(*Locators.REG_BUTTON_FINALE).click()
        error = driver.find_element(*Locators.PASSWORD_ERROR).text
        assert error == 'Некорректный пароль'
        
         
        
        



       



