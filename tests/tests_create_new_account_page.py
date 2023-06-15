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
import tests_functions as function


class TestAccountCreatingForm(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = tests_credentials
        self.locators = tests_site_locators

    def test_create_account_page_loads_up(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.create_new_account_page_load_up_assert(self)

    def test_creating_account_no_name(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password(self, "ok")
        function.account_page_fill_repeat_password(self, "ok")
        function.account_page_submit_button_click(self)
        function.account_page_no_name_assert(self)

    def test_creating_account_no_lastname(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password(self, "ok")
        function.account_page_fill_repeat_password(self, "ok")
        function.account_page_submit_button_click(self)
        function.account_page_no_lastname_assert(self)

    def test_creating_account_no_mail(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_password(self, "ok")
        function.account_page_fill_repeat_password(self, "ok")
        function.account_page_submit_button_click(self)
        function.account_page_no_mail_assert(self)

    def test_creating_account_password_to_short(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password_too_short(self)

    def test_creating_account_password_no_special_char(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password(self, "no special char")
        sleep(1)
        function.account_page_password_no_special_char_assert(self)

    def test_creating_account_password_not_match(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password(self, "ok")
        function.account_page_fill_repeat_password(self, "ok different")
        function.account_page_submit_button_click(self)
        sleep(1)
        function.account_page_password_not_match_assert(self)

    def test_creating_account_password_weak(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password(self, "weak")
        sleep(1)
        function.account_page_password_weak_assert(self)

    def test_creating_account_password_medium(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password(self, "medium")
        sleep(1)
        function.account_page_password_medium_assert(self)

    def test_creating_account_password_strong(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password(self, "strong")
        sleep(1)
        function.account_page_password_strong_assert(self)

    def test_creating_account_password_very_strong(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password(self, "very strong")
        sleep(1)
        function.account_page_password_very_hard_assert(self)

    def test_creating_account_but_mail_already_existing(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail_existing_and_valid(self)
        function.account_page_fill_password(self, "ok")
        function.account_page_fill_repeat_password(self, "ok")
        function.account_page_submit_button_click(self)
        sleep(2)
        function.account_page_create_account_but_mail_already_existing_assert(self)


"""  Due to assertion method, this will be only positive when creating the account for first time
    def test_creating_account_positive(self):
        function.goto_main_page(self)
        function.goto_create_account_page(self)
        function.account_page_fill_firstname(self)
        function.account_page_fill_lastname(self)
        function.account_page_fill_mail(self)
        function.account_page_fill_password(self, "ok")
        function.account_page_fill_repeat_password(self, "ok")
        function.account_page_submit_button_click(self)
        sleep(2)
        cfunction.heck_if_John_Doe_logged_in(self)
"""


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
