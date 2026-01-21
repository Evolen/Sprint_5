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
       assert login_home_page == True       
       WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//*[text() = 'Оформить заказ']"))) 
       driver.quit() 
#Проверка входа из личного кабинета
class TestLoginPersonalAccount:
    def test_login_personal_acc(self, driver,login_personal_acc):
        assert login_personal_acc == True
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, ".//*[text() = 'Оформить заказ']"))) 
        driver.quit()
#Проверка входа через кнопку в форме регистрации
class TestLoginRegistration:
    def test_login_registration(self, driver, login_registration):
        assert login_registration == True        
        driver.find_element(*Locators.EMAIL).send_keys("grimm39@yandex.ru")          
        driver.find_element(*Locators.PASSWORD_LOGIN).send_keys("123456")        
        driver.find_element(*Locators.LOGIN_BUTTON_FINALLY).click()  
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text() = 'Оформить заказ']"))) 
        driver.quit()    
#Проверка входа через кнопку в форме восстановления пароля.
class TestLoginPasswordRecovery:
    def test_login_pass_recovery (self, driver, login_pass_recovery):
        assert login_pass_recovery == True        
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text() = 'Оформить заказ']"))) 
        driver.quit()
