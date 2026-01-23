from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from selenium.webdriver.common.by import By
import pytest

#Проверка выхода
class TestExit:
    def test_exit(self, driver,login_home_page):
         
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.EXIT_BUTTON))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        exit_check = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.CHECK_FORM_ENTRANCE)).text
        assert exit_check == "Вход"
        