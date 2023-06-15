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
import tests_functions as function


class TestAccountCreatingForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = tests_credentials
        self.locators = tests_site_locators

    def test_sign_in_page_load_up(self):
        function.goto_main_page(self)
        function.goto_sign_in_page(self)
        function.sign_in_page_load_up_assert(self)

    def test_sign_in_to_existing_account(self):
        function.goto_main_page(self)
        function.goto_sign_in_page(self)
        function.sign_in_page_fill_in_mail(self)
        function.sign_in_page_fill_in_password(self)
        function.sign_in_page_sign_in_button_click(self)
        sleep(4)
        function.sign_in_to_existing_account_assert(self)

    def test_sign_in_and_logout(self):
        function.goto_main_page(self)
        function.goto_sign_in_page(self)
        function.sign_in_page_fill_in_mail(self)
        function.sign_in_page_fill_in_password(self)
        function.sign_in_page_sign_in_button_click(self)
        function.sign_in_page_logout(self)
        function.sign_in_page_sign_in_and_logout_assert(self)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
