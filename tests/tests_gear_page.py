# zbior testow dla podstrony gear/bags

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
import tests_credentials
import tests_site_locators
from tests_functions import *


class TestGearPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = tests_credentials
        self.locators = tests_site_locators

    def test_gear_bags_page_shows_up(self):
        goto_main_page(self)
        goto_gear_bags(self)
        gear_bags_page_shows_up_assert(self)

    def test_gear_bags_pages_are_full_except_last(self):
        goto_main_page(self)
        goto_gear_bags(self)
        sleep(2)
        output = item_pages_are_full_except_last_test(self)
        item_pages_are_full_except_last_assert(
            self, output[0], output[1], output[2], output[3]
        )


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
