# projekt bedzie opieral sie o testowanie funkcjonalnosci strony magento.softwaretestingboard.com/ z wykorzystaniem biblioteki selenium

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

    def test_creating_account_no_name(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_lastname(self)
        account_page_fill_mail(self)
        account_page_fill_password(self, "ok")
        account_page_fill_repeat_password(self, "ok")
        account_page_submit_button_click(self)
        account_page_no_name_assert(self)

    def test_creating_account_no_lastname(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_mail(self)
        account_page_fill_password(self, "ok")
        account_page_fill_repeat_password(self, "ok")
        account_page_submit_button_click(self)
        account_page_no_lastname_assert(self)

    def test_creating_account_no_mail(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_password(self, "ok")
        account_page_fill_repeat_password(self, "ok")
        account_page_submit_button_click(self)
        account_page_no_mail_assert(self)

    def test_creating_account_password_to_short(self):
        driver = self.driver
        # wait = self.wait
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_mail(self)
        account_page_fill_password_too_short(self)

    def test_creating_account_password_no_special_char(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_mail(self)
        account_page_fill_password(self, "no special char")
        sleep(1)
        account_page_password_no_special_char_assert(self)

    def test_creating_account_password_not_match(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_mail(self)
        account_page_fill_password(self, "ok")
        account_page_fill_repeat_password(self, "ok different")
        account_page_submit_button_click(self)
        sleep(1)
        account_page_password_not_match_assert(self)

    def test_creating_account_password_weak(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_mail(self)
        account_page_fill_password(self, "weak")
        sleep(1)
        account_page_password_weak_assert(self)

    def test_creating_account_password_medium(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_mail(self)
        account_page_fill_password(self, "medium")
        sleep(1)
        account_page_password_medium_assert(self)

    def test_creating_account_password_strong(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_mail(self)
        account_page_fill_password(self, "strong")
        sleep(1)
        account_page_password_strong_assert(self)

    def test_creating_account_password_very_strong(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_mail(self)
        account_page_fill_password(self, "very strong")
        sleep(1)
        account_page_password_very_hard_assert(self)

    def test_creating_account_but_mail_already_existing(self):
        driver = self.driver
        goto_main_page(self)
        goto_create_account_page(self)
        account_page_fill_firstname(self)
        account_page_fill_lastname(self)
        account_page_fill_mail_existing_and_valid(self)
        account_page_fill_password(self, "ok")
        account_page_fill_repeat_password(self, "ok")
        account_page_submit_button_click(self)
        sleep(2)
        account_page_create_account_but_mail_already_existing_assert(self)

    def test_sign_in_to_existing_account(self):
        driver = self.driver
        goto_main_page(self)
        goto_sign_in_page(self)
        sign_in_page_fill_in_mail(self)
        sign_in_page_fill_in_password(self)
        sign_in_page_sign_in_button_click(self)
        sleep(4)
        sign_in_to_existing_account_assert(self)


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
