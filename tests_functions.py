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


def goto_main_page(self):
    driver = self.driver
    driver.get(self.locators.main_page_adress)


def sign_in_page_sign_in_button_click(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="send2"]/span').click()


def login_to_account(self):
    driver = self.driver
    goto_main_page(self)
    if check_if_John_Doe_logged_in(self):
        print("Użytkownik zalogowany, kontynuacja")
    else:
        print("Użytkownik niezalogowany, logowanie")
        goto_sign_in_page(self)
        sign_in_page_fill_in_mail(self)
        sign_in_page_fill_in_password(self)
        sign_in_page_sign_in_button_click(self)
    sleep(2)


def check_if_John_Doe_logged_in(self):
    driver = self.driver
    sleep(2)
    return (
        driver.find_element(By.XPATH, self.locators.main_page_welcome_message_id).text
        == "Welcome, John Doe!"
    )


def sign_in_page_fill_in_mail(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.sign_in_page_mail_id).send_keys(
        self.dane.account_data_valid("mail")
    )


def sign_in_page_fill_in_password(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.sign_in_page_password_id).send_keys(
        self.dane.account_data_valid("password")
    )


def goto_account_data(self):
    driver = self.driver
    driver.find_element(
        By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[2]/span/button"
    ).click()
    driver.find_element(
        By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[2]/div/ul/li[1]/a"
    ).click()


def goto_shipping_adress_page(self):
    driver = self.driver
    driver.find_element(
        By.XPATH, '//*[@data-ui-id="default-shipping-edit-link"]'
    ).click()


def goto_sign_in_page(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.main_page_sign_in_button_id).click()


def clean_cart(self):
    driver = self.driver
    sleep(2)
    # cleaning
    driver.find_element(
        By.XPATH, '//*[@id="mini-cart"]/li[1]/div/div/div[3]/div[2]/a'
    ).click()
    sleep(2)
    driver.find_element(
        By.XPATH, "/html/body/div[3]/aside[2]/div[2]/footer/button[2]"
    ).click()
    sleep(3)


def goto_create_account_page(self):
    driver = self.driver
    driver.find_element(
        By.XPATH, self.locators.main_page_create_account_button_id
    ).click()


def account_page_fill_firstname(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.register_firstname_id).send_keys(
        self.dane.test_firstname()
    )


def account_page_fill_lastname(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.register_lastname_id).send_keys(
        self.dane.test_surname()
    )


def account_page_fill_mail(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.register_mail_id).send_keys(
        self.dane.test_mail()
    )


def account_page_fill_mail_existing_and_valid(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.register_mail_id).send_keys(
        self.dane.account_data_valid("mail")
    )


def account_page_fill_password(self, type):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.register_password_id).send_keys(
        self.dane.test_password(type)
    )


def account_page_fill_repeat_password(self, type):
    driver = self.driver
    driver.find_element(
        By.XPATH, self.locators.register_password_confirmation_id
    ).send_keys(self.dane.test_password(type))


def account_page_submit_button_click(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.account_page_submit_button_id).click()


def account_page_fill_password_too_short(self):
    driver = self.driver
    for password_length in range(7):
        driver.find_element(By.XPATH, self.locators.register_password_id).send_keys("a")
        sleep(0.5)
        password_length += 1
        if (
            driver.find_element(
                By.XPATH, self.locators.create_account_password_error_id
            ).text
            == "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored."
        ):
            continue
        else:
            assert False
    assert True


def account_page_no_name_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.create_account_firstname_error_id
        ).get_attribute("generated")
        == "true"
    )


def account_page_no_lastname_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.create_account_lastname_error_id
        ).get_attribute("generated")
        == "true"
    )


def account_page_no_mail_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.create_account_mail_error_id
        ).get_attribute("generated")
        == "true"
    )


def account_page_password_no_special_char_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.create_account_password_error_id
        ).text
        == "Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters."
    )


def account_page_password_not_match_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.create_account_repeat_password_error_id
        ).text
        == "Please enter the same value again."
    )


def account_page_password_weak_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.create_account_password_strength_meter_label_id
        ).text
        == "Weak"
    )


def account_page_password_medium_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.create_account_password_strength_meter_label_id
        ).text
        == "Medium"
    )


def account_page_password_strong_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.create_account_password_strength_meter_label_id
        ).text
        == "Strong"
    )


def account_page_password_very_hard_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.create_account_password_strength_meter_label_id
        ).text
        == "Very Strong"
    )


def account_page_create_account_but_mail_already_existing_assert(self):
    driver = self.driver
    assert EC.visibility_of(
        driver.find_element(
            By.XPATH, self.locators.create_account_mail__already_existing_id
        )
    )


def sign_in_to_existing_account_assert(self):
    driver = self.driver
    assert (
        driver.find_element(By.XPATH, self.locators.main_page_welcome_message_id).text
        == "Welcome, "
        + self.dane.account_data_valid("name")
        + " "
        + self.dane.account_data_valid("surname")
        + "!"
    )


def main_page_title_assert(self):
    driver = self.driver
    assert driver.title == "Home Page"


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
