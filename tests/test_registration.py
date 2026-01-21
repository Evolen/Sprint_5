from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By
import pytest


#Проверка регистрации      
class TestRegistration:
    def test_registration(self, driver,login_registration):

        assert login_registration == True 
        #WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text() = 'Вход']")))
        driver.quit()       

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
        assert error == "Некорректный пароль"
        driver.quit() 
        
        



       



