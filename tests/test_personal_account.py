from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By
#import requests
import pytest

#Проверка перехода в личный кабинет
class TestPersonalAccaunt:
    def test_personal_acc(self, driver, login_home_page):
        assert login_home_page == True
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//*[text() = 'Профиль']"))) 
        driver.quit() 