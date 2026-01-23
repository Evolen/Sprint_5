from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
import pytest

#Проверка перехода к разделу "Булки", "Соусы", "Начинки"
class TestSections:
    def test_sections_sauces(self, driver):
        driver.find_element(*Locators.SAUCES).click()
        sauces_check = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.SAUCES_CHOICE)).text   
        assert sauces_check == "Соусы"

    def test_sections_fillings(self, driver):
        driver.find_element(*Locators.FILLINGS).click()
        fillings_check = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.FILLINGS_CHOICE)).text 
        assert fillings_check == "Начинки"

    def test_sections_bun(self, driver):
        driver.find_element(*Locators.SAUCES).click()  
        driver.find_element(*Locators.BUN).click()
        bun_check = WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(Locators.BUN_CHOICE)).text 
        assert bun_check == "Булки"
        