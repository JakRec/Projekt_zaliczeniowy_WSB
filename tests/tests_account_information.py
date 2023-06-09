# account information tests https://magento.softwaretestingboard.com/customer/account/
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


class TestAccountInformation(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = tests_credentials
        self.locators = tests_site_locators

    def test_account_informations_page_load_up(self):
        function.goto_main_page(self)
        function.login_to_account(self)
        function.goto_account_data(self)
        function.goto_account_informations(self)
        function.account_informations_page_load_up_assert(self)

    def test_account_informations_page_change_mail_form_shows_up(self):
        function.goto_main_page(self)
        function.login_to_account(self)
        function.goto_account_data(self)
        function.goto_account_informations(self)
        function.account_informations_page_change_mail_click(self)
        function.account_informations_page_change_mail_assert(self)

    def test_account_informations_page_change_password_form_shows_up(self):
        function.goto_main_page(self)
        function.login_to_account(self)
        function.goto_account_data(self)
        function.goto_account_informations(self)
        function.account_informations_page_change_password_click(self)
        function.account_informations_page_change_password_assert(self)

    def test_account_informations_page_change_mail_and_password_form_shows_up(self):
        function.goto_main_page(self)
        function.login_to_account(self)
        function.goto_account_data(self)
        function.goto_account_informations(self)
        function.account_informations_page_change_mail_click(self)
        function.account_informations_page_change_password_click(self)
        function.account_informations_page_change_mail_and_password_assert(self)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
