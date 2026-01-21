from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import pytest

#Проверка перехода к разделу "Булки", "Соусы", "Начинки"
class TestSections:
    def test_sections(self, driver):
         
        driver.find_element(*Locators.SAUCES).click()
        driver.find_element(*Locators.FILLINGS).click()
        driver.find_element(*Locators.BUN).click()
        driver.quit()