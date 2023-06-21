# tests for shop functionalities https://magento.softwaretestingboard.com/
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
import tests_credentials
import tests_site_locators
import tests_functions as function


class TestShopFunctionality(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = tests_credentials
        self.locators = tests_site_locators

    def test_cart_adding(self):
        function.login_to_account(self)
        function.open_cart(self)
        sleep(1)
        function.cart_clean_cart(self)
        function.main_page_add_to_cart_blue_shirt(self)
        sleep(3)
        function.cart_adding_item_assert(self)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
