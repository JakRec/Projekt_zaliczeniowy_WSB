# zbior testow dla strony glownej

# wczytanie bibliotek
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

    def test_website_opening(self):
        driver = self.driver
        goto_main_page(self)
        main_page_title_assert(self)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)

"""  Due to assertion method, this will be only positive when creating the account for first time
    def test_creating_account_positive(self):
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_mail(self)
        account_page_fill_password(self, "ok")
        account_page_fill_repeat_password(self, "ok")
        account_page_submit_button_click(self)
        sleep(2)
        check_if_John_Doe_logged_in(self)
"""
