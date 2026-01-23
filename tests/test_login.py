from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By
import pytest

#Проверка входа с главной страницы
class TestLoginHomePage:
    def test_login_home_page(self, driver, login_home_page):
             
       home_page = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER )).text 
       assert home_page == 'Оформить заказ'
       
#Проверка входа из личного кабинета
class TestLoginPersonalAccount:
    def test_login_personal_acc(self, driver,login_personal_acc):
        acc_page = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER )).text 
        assert acc_page == 'Оформить заказ'
         
        
#Проверка входа через кнопку в форме регистрации
class TestLoginRegistration:
    def test_login_registration(self, driver, login_registration):
              
        driver.find_element(*Locators.EMAIL).send_keys("grimm39@yandex.ru")          
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys("123456")        
        driver.find_element(*Locators.LOGIN_BUTTON_FINALLY).click()  
        reg_page = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER )).text 
        assert reg_page == 'Оформить заказ' 
           
#Проверка входа через кнопку в форме восстановления пароля.
class TestLoginPasswordRecovery:
    def test_login_pass_recovery (self, driver, login_pass_recovery):
        pass_page = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUTTON_ORDER )).text 
        assert pass_page == 'Оформить заказ'        
        
        
