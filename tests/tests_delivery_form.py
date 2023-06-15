# zbior testow formularza do wysylki na stronie magento.softwaretestingboard.com/

# wczytanie bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
import tests_credentials
import tests_site_locators
import tests_functions as function


class TestDeliveryForm(unittest.TestCase):
    def setUp(self):
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = tests_credentials
        self.locators = tests_site_locators

    def test_user_data_viability_check(self):
        function.login_to_account(self)
        function.goto_account_data(self)
        function.user_data_viability_check_assert(self)

    def test_delivery_adress_no_firstname(self):
        function.login_to_account(self)
        function.goto_account_data(self)
        function.goto_shipping_adress_page(self)
        function.delivery_adress_page_clean_firstname_and_lastname(self)
        function.delivery_adress_page_fill_lastname(self)
        function.delivery_adress_page_fill_telephone(self)
        function.delivery_adress_page_fill_adress(self)
        function.delivery_adress_page_fill_city(self)
        function.delivery_adress_page_fill_region(self)
        function.delivery_adress_page_fill_postal_code(self)
        function.delivery_adress_page_fill_country(self)
        function.delivery_adress_page_save_adress_button_click(self)
        function.delivery_adress_no_firstname_assert(self)

    def test_delivery_adress_no_lastname(self):
        function.login_to_account(self)
        function.goto_account_data(self)
        function.goto_shipping_adress_page(self)
        function.delivery_adress_page_clean_firstname_and_lastname(self)
        function.delivery_adress_page_fill_firstname(self)
        function.delivery_adress_page_fill_telephone(self)
        function.delivery_adress_page_fill_adress(self)
        function.delivery_adress_page_fill_city(self)
        function.delivery_adress_page_fill_region(self)
        function.delivery_adress_page_fill_postal_code(self)
        function.delivery_adress_page_fill_country(self)
        function.delivery_adress_page_save_adress_button_click(self)
        function.delivery_adress_no_lastname_assert(self)

    def test_delivery_adress_no_phone_number(self):
        function.login_to_account(self)
        function.goto_account_data(self)
        function.goto_shipping_adress_page(self)
        function.delivery_adress_page_clean_firstname_and_lastname(self)
        function.delivery_adress_page_fill_firstname(self)
        function.delivery_adress_page_fill_lastname(self)
        function.delivery_adress_page_fill_adress(self)
        function.delivery_adress_page_fill_city(self)
        function.delivery_adress_page_fill_region(self)
        function.delivery_adress_page_fill_postal_code(self)
        function.delivery_adress_page_fill_country(self)
        function.delivery_adress_page_save_adress_button_click(self)
        function.delivery_adress_no_telephone_assert(self)

    def test_delivery_adress_no_adress(self):
        # error occurs only with no input in first row
        function.login_to_account(self)
        function.goto_account_data(self)
        function.goto_shipping_adress_page(self)
        function.delivery_adress_page_clean_firstname_and_lastname(self)
        function.delivery_adress_page_fill_firstname(self)
        function.delivery_adress_page_fill_lastname(self)
        function.delivery_adress_page_fill_telephone(self)
        function.delivery_adress_page_fill_city(self)
        function.delivery_adress_page_fill_region(self)
        function.delivery_adress_page_fill_postal_code(self)
        function.delivery_adress_page_fill_country(self)
        function.delivery_adress_page_save_adress_button_click(self)
        function.delivery_adress_no_adress_assert(self)

    def test_delivery_adress_no_city(self):
        function.login_to_account(self)
        function.goto_account_data(self)
        function.goto_shipping_adress_page(self)
        function.delivery_adress_page_clean_firstname_and_lastname(self)
        function.delivery_adress_page_fill_firstname(self)
        function.delivery_adress_page_fill_lastname(self)
        function.delivery_adress_page_fill_telephone(self)
        function.delivery_adress_page_fill_adress(self)
        function.delivery_adress_page_fill_region(self)
        function.delivery_adress_page_fill_postal_code(self)
        function.delivery_adress_page_fill_country(self)
        function.delivery_adress_page_save_adress_button_click(self)
        function.delivery_adress_no_city_assert(self)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
