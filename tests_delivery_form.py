# zbior testow formularza do wysylki na stronie magento.softwaretestingboard.com/

# wczytanie bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

# from selenium.webdriver.support import expected_conditions as EC biblioteka na ten moment nie uzywana
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
import tests_credentials
import tests_site_locators
from tests_functions import *


def user_data_viability_check_assert(self):
    driver = self.driver
    assert driver.find_element(
        By.XPATH,
        '//*[@id="maincontent"]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/p',
    ).text == self.dane.account_data_valid("name") + " " + self.dane.account_data_valid(
        "surname"
    ) + "\n" + self.dane.account_data_valid(
        "mail"
    )


def delivery_adress_page_clean_firstname_and_lastname(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="firstname"]').clear()
    driver.find_element(By.XPATH, '//*[@id="lastname"]').clear()


def delivery_adress_page_fill_firstname(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="firstname"]').send_keys(
        self.dane.account_data_valid("name")
    )


def delivery_adress_page_fill_lastname(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="lastname"]').send_keys(
        self.dane.account_data_valid("surname")
    )


def delivery_adress_page_fill_telephone(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="telephone"]').send_keys(
        self.dane.account_data_valid("phone")
    )


def delivery_adress_page_fill_adress(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="street_1"]').send_keys(
        self.dane.account_data_valid("adress")
    )


def delivery_adress_page_fill_city(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(
        self.dane.account_data_valid("city")
    )


def delivery_adress_page_fill_region(self):
    driver = self.driver
    Select(
        driver.find_element(By.XPATH, '//*[@id="region_id"]')
    ).select_by_visible_text("Arizona")


def delivery_adress_page_fill_postal_code(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="zip"]').send_keys(
        self.dane.account_data_valid("postal_code")
    )


def delivery_adress_page_fill_country(self):
    driver = self.driver
    Select(driver.find_element(By.XPATH, '//*[@id="country"]')).select_by_visible_text(
        self.dane.account_data_valid("country")
    )
    driver.find_element(By.XPATH, '//*[@title="Save Address"]').click()


def delivery_adress_page_save_adress_button_click(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@title="Save Address"]').click()


def delivery_adress_no_firstname_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, '//*[@id="firstname-error"]')


def delivery_adress_no_lastname_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, '//*[@id="lastname-error"]')


def delivery_adress_no_telephone_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, '//*[@id="telephone-error"]')


def delivery_adress_no_adress_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, '//*[@id="street_1-error"]')


def delivery_adress_no_city_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, '//*[@id="city-error"]')


def open_cart(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@class="action showcart"]').click()


def cart_clean_cart(self):
    driver = self.driver
    if (
        driver.find_element(
            By.XPATH, '//*[@id="minicart-content-wrapper"]/div[2]/strong'
        ).text
        != "You have no items in your shopping cart."
    ):
        print("czyszczenie koszyka")
        clean_cart(self)
        print("wyczyszczono koszyk")
    else:
        pass


def main_page_add_to_cart_blue_shirt(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="option-label-size-143-item-166"]').click()
    driver.find_element(By.XPATH, '//*[@id="option-label-color-93-item-50"]').click()
    driver.find_element(
        By.XPATH,
        '//*[@id="maincontent"]/div[3]/div/div[2]/div[3]/div/div/ol/li[1]/div/div/div[4]/div/div[1]/form/button',
    ).click()


def cart_adding_item_assert(self):
    driver = self.driver
    assert (
        int(
            driver.find_element(
                By.XPATH, "/html/body/div[1]/header/div[2]/div[1]/a/span[2]/span[1]"
            ).text
        )
        == 1
    )


class TestDeliveryForm(unittest.TestCase):
    driver = webdriver.Chrome()

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = tests_credentials
        self.locators = tests_site_locators

    def test_user_data_viability_check(self):
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        user_data_viability_check_assert(self)

    def test_delivery_adress_no_firstname(self):
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        delivery_adress_page_clean_firstname_and_lastname(self)
        delivery_adress_page_fill_lastname(self)
        delivery_adress_page_fill_telephone(self)
        delivery_adress_page_fill_adress(self)
        delivery_adress_page_fill_city(self)
        delivery_adress_page_fill_region(self)
        delivery_adress_page_fill_postal_code(self)
        delivery_adress_page_fill_country(self)
        delivery_adress_page_save_adress_button_click(self)
        delivery_adress_no_firstname_assert(self)

    def test_delivery_adress_no_lastname(self):
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        delivery_adress_page_clean_firstname_and_lastname(self)
        delivery_adress_page_fill_firstname(self)
        delivery_adress_page_fill_telephone(self)
        delivery_adress_page_fill_adress(self)
        delivery_adress_page_fill_city(self)
        delivery_adress_page_fill_region(self)
        delivery_adress_page_fill_postal_code(self)
        delivery_adress_page_fill_country(self)
        delivery_adress_page_save_adress_button_click(self)
        delivery_adress_no_lastname_assert(self)

    def test_delivery_adress_no_phone_number(self):
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        delivery_adress_page_clean_firstname_and_lastname(self)
        delivery_adress_page_fill_firstname(self)
        delivery_adress_page_fill_lastname(self)
        delivery_adress_page_fill_adress(self)
        delivery_adress_page_fill_city(self)
        delivery_adress_page_fill_region(self)
        delivery_adress_page_fill_postal_code(self)
        delivery_adress_page_fill_country(self)
        delivery_adress_page_save_adress_button_click(self)
        delivery_adress_no_telephone_assert(self)

    def test_delivery_adress_no_adress(self):
        # error occurs only with no input in first row
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        delivery_adress_page_clean_firstname_and_lastname(self)
        delivery_adress_page_fill_firstname(self)
        delivery_adress_page_fill_lastname(self)
        delivery_adress_page_fill_telephone(self)
        delivery_adress_page_fill_city(self)
        delivery_adress_page_fill_region(self)
        delivery_adress_page_fill_postal_code(self)
        delivery_adress_page_fill_country(self)
        delivery_adress_page_save_adress_button_click(self)
        delivery_adress_no_adress_assert(self)

    def test_delivery_adress_no_city(self):
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        delivery_adress_page_clean_firstname_and_lastname(self)
        delivery_adress_page_fill_firstname(self)
        delivery_adress_page_fill_lastname(self)
        delivery_adress_page_fill_telephone(self)
        delivery_adress_page_fill_adress(self)
        delivery_adress_page_fill_region(self)
        delivery_adress_page_fill_postal_code(self)
        delivery_adress_page_fill_country(self)
        delivery_adress_page_save_adress_button_click(self)
        delivery_adress_no_city_assert(self)

    def test_cart_adding(self):
        driver = self.driver
        login_to_account(self)
        open_cart(self)
        sleep(1)
        cart_clean_cart(self)
        main_page_add_to_cart_blue_shirt(self)
        sleep(3)
        cart_adding_item_assert(self)


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
