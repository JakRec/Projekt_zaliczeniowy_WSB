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


def goto_gear_bags(self):
    driver = self.driver
    action = self.action
    action.move_to_element(driver.find_element(By.XPATH, '//*[@id="ui-id-6"]')).click(
        driver.find_element(By.XPATH, '//*[@id="ui-id-25"]')
    ).perform()


def gear_bags_page_shows_up_assert(self):
    driver = self.driver
    assert driver.title == "Bags - Gear"


def item_page_find_how_many_items_for_sale_max(self):
    driver = self.driver
    return int(driver.find_element(By.XPATH, '//*[@id="toolbar-amount"]/span[3]').text)


def item_page_find_all_items_for_sale(self):
    driver = self.driver
    return len(driver.find_elements(By.XPATH, '//a[@class="product-item-link"]'))


def gear_bags_page_is_full_assert(self):
    if item_page_find_how_many_items_for_sale_max(self) >= 12:
        assert item_page_find_all_items_for_sale(self) == 12
    else:
        assert item_page_find_how_many_items_for_sale_max(
            self
        ) == item_page_find_all_items_for_sale(self)


def gear_bags_page_goto_next_page(self):
    driver = self.driver
    driver.find_element(
        By.XPATH,
        '//*[@id="maincontent"]/div[3]/div[1]/div[4]/div[2]/ul/li[2]/a',
    ).click()


def gear_bags_pages_are_full_except_last_test_and_assert(self):
    if item_page_find_how_many_items_for_sale_max(self) >= 12:
        predicted_last_page_items_number = (
            item_page_find_how_many_items_for_sale_max(self) % 12
        )
        pages_number = item_page_find_how_many_items_for_sale_max(self) // 12 + 1
        current_page = 1
        total_items_number = 0
        for current_page in range(current_page, pages_number + 1):
            total_items_number += item_page_find_all_items_for_sale(self)
            print(
                "At page number: "
                + str(current_page)
                + " present: "
                + str(item_page_find_all_items_for_sale(self))
                + " elements"
            )
            if current_page == pages_number:
                actual_last_page_items_number = item_page_find_all_items_for_sale(self)
            else:
                current_page += 1
                gear_bags_page_goto_next_page(self)
                sleep(2)
        print("total elements in category: " + str(total_items_number))
        print("elements on last page: " + str(actual_last_page_items_number))
        assert (
            item_page_find_how_many_items_for_sale_max(self) == total_items_number
            and predicted_last_page_items_number == actual_last_page_items_number
        )
    else:
        assert item_page_find_how_many_items_for_sale_max(
            self
        ) == item_page_find_all_items_for_sale(self)


class TestGearPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = tests_credentials
        self.locators = tests_site_locators

    def test_gear_bags_page_shows_up(self):
        driver = self.driver
        goto_main_page(self)
        goto_gear_bags(self)
        gear_bags_page_shows_up_assert(self)

    def test_gear_bags_pages_are_full_except_last(self):
        driver = self.driver
        goto_main_page(self)
        goto_gear_bags(self)
        sleep(2)
        gear_bags_pages_are_full_except_last_test_and_assert(self)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
