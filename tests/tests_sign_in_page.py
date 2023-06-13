# zbior testow dla podstrony logowania
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
import tests_credentials
import tests_site_locators
from tests_functions import *


class TestAccountCreatingForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = tests_credentials
        self.locators = tests_site_locators

    def test_sign_in_page_load_up(self):
        driver = self.driver
        goto_main_page(self)
        goto_sign_in_page(self)
        sign_in_page_load_up_assert(self)

    def test_sign_in_to_existing_account(self):
        driver = self.driver
        goto_main_page(self)
        goto_sign_in_page(self)
        sign_in_page_fill_in_mail(self)
        sign_in_page_fill_in_password(self)
        sign_in_page_sign_in_button_click(self)
        sleep(4)
        sign_in_to_existing_account_assert(self)

    def test_sign_in_and_logout(self):
        driver = self.driver
        goto_main_page(self)
        goto_sign_in_page(self)
        sign_in_page_fill_in_mail(self)
        sign_in_page_fill_in_password(self)
        sign_in_page_sign_in_button_click(self)
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[2]/span/button"
        ).click()
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[2]/div/ul/li[3]/a"
        ).click()
        driver.find_element(
            By.XPATH, '//*[@id="maincontent"]/div[1]/h1/span'
        ) == "You are signed out"


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
