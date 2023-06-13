# funkcje wykorzystywane w testach

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
    driver.find_element(By.XPATH, self.locators.sign_in_page_sign_in_button_id).click()


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
        By.XPATH, self.locators.main_page_account_options_expand_id
    ).click()
    driver.find_element(
        By.XPATH, self.locators.main_page_account_options_expanded_open_account_data_id
    ).click()


def create_new_account_page_load_up_assert(self):
    driver = self.driver
    assert driver.title() == self.locators.create_account_page_title


def sign_in_page_load_up_assert(self):
    driver = self.driver
    assert driver.title() == self.locators.sign_in_page_title


def goto_shipping_adress_page(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.account_page_shipping_adress_id).click()


def goto_sign_in_page(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.main_page_sign_in_button_id).click()


def clean_cart(self):
    driver = self.driver
    sleep(2)
    # cleaning
    driver.find_element(By.XPATH, self.locators.main_page_mini_cart_expand_id).click()
    sleep(2)
    driver.find_element(
        By.XPATH, self.locators.main_page_mini_cart_clean_cart_button_id
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
    driver.find_element(By.XPATH, self.locators.delivery_page_firstname_id).clear()
    driver.find_element(By.XPATH, self.locators.delivery_page_lastname_id).clear()


def delivery_adress_page_fill_firstname(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.delivery_page_firstname_id).send_keys(
        self.dane.account_data_valid("name")
    )


def delivery_adress_page_fill_lastname(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.delivery_page_lastname_id).send_keys(
        self.dane.account_data_valid("surname")
    )


def delivery_adress_page_fill_telephone(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.delivery_page_telephone_id).send_keys(
        self.dane.account_data_valid("phone")
    )


def delivery_adress_page_fill_adress(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.delivery_page_street_id).send_keys(
        self.dane.account_data_valid("adress")
    )


def delivery_adress_page_fill_city(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.delivery_page_city_id).send_keys(
        self.dane.account_data_valid("city")
    )


def delivery_adress_page_fill_region(self):
    driver = self.driver
    Select(
        driver.find_element(By.XPATH, self.locators.delivery_page_region_id)
    ).select_by_visible_text("Arizona")


def delivery_adress_page_fill_postal_code(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.delivery_page_zip_code_id).send_keys(
        self.dane.account_data_valid("postal_code")
    )


def delivery_adress_page_fill_country(self):
    driver = self.driver
    Select(
        driver.find_element(By.XPATH, self.locators.delivery_page_country_id)
    ).select_by_visible_text(self.dane.account_data_valid("country"))
    driver.find_element(By.XPATH, '//*[@title="Save Address"]').click()


def delivery_adress_page_save_adress_button_click(self):
    driver = self.driver
    driver.find_element(
        By.XPATH, self.locators.delivery_page_save_adress_button_id
    ).click()


def delivery_adress_no_firstname_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, self.locators.delivery_page_firstname_error_id)


def delivery_adress_no_lastname_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, self.locators.delivery_page_lastname_error_id)


def delivery_adress_no_telephone_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, self.locators.delivery_page_telephone_error_id)


def delivery_adress_no_adress_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, self.locators.delivery_page_street_error_id)


def delivery_adress_no_city_assert(self):
    driver = self.driver
    assert driver.find_element(By.XPATH, self.locators.delivery_page_city_error_id)


def open_cart(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.open_cart_button_id).click()


def cart_clean_cart(self):
    driver = self.driver
    if (
        driver.find_element(By.XPATH, self.locators.cart_content_no_content).text
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
                By.XPATH, self.locators.cart_content_content_number
            ).text
        )
        == 1
    )


def goto_account_informations(self):
    driver = self.driver
    driver.find_element(By.XPATH, self.locators.account_page_go_to_acc_page_id).click()


def account_informations_page_load_up_assert(self):
    driver = self.driver
    assert driver.title == self.locators.account_information_page_title


def account_informations_page_change_mail_click(self):
    driver = self.driver
    driver.find_element(
        By.XPATH, self.locators.account_information_page_change_email_id
    ).click()


def account_informations_page_change_mail_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.account_information_page_change_mail_password_id
        ).is_displayed()
        and driver.find_element(
            By.XPATH, self.locators.account_information_page_change_mail_password_id
        ).text
        == "Change Email"
    )


def account_informations_page_change_password_click(self):
    driver = self.driver
    driver.find_element(
        By.XPATH, self.locators.account_information_page_change_password_id
    ).click()


def account_informations_page_change_password_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.account_information_page_change_mail_password_id
        ).is_displayed()
        and driver.find_element(
            By.XPATH, self.locators.account_information_page_change_mail_password_id
        ).text
        == "Change Password"
    )


def account_informations_page_change_mail_and_password_assert(self):
    driver = self.driver
    assert (
        driver.find_element(
            By.XPATH, self.locators.account_information_page_change_mail_password_id
        ).is_displayed()
        and driver.find_element(
            By.XPATH, self.locators.account_information_page_change_mail_password_id
        ).text
        == "Change Email and Password"
    )


def goto_gear_bags(self):
    driver = self.driver
    action = self.action
    action.move_to_element(
        driver.find_element(By.XPATH, self.locators.main_page_gear_menu_expand_id)
    ).click(
        driver.find_element(
            By.XPATH, self.locators.main_page_gear_menu_expanded_bags_id
        )
    ).perform()


def gear_bags_page_shows_up_assert(self):
    driver = self.driver
    assert driver.title == self.locators.gear_bags_page_titl


def item_page_find_how_many_items_for_sale_max(self):
    driver = self.driver
    return int(
        driver.find_element(By.XPATH, self.locators.gear_bags_page_item_counter_id).text
    )


def item_page_find_all_items_for_sale(self):
    driver = self.driver
    return len(driver.find_elements(By.XPATH, self.locators.gear_bags_page_any_item_id))


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
        self.locators.gear_bags_page_next_page_button_id,
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


def item_pages_are_full_except_last_test(self):
    max_items_on_page = item_page_find_how_many_items_for_sale_max(self)
    predicted_last_page_items_number = (
        item_page_find_how_many_items_for_sale_max(self) % 12
    )
    pages_number = item_page_find_how_many_items_for_sale_max(self) // 12 + 1
    print(pages_number)
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
            sleep(1)
    print("total elements in category: " + str(total_items_number))
    print("elements on last page: " + str(actual_last_page_items_number))
    return (
        total_items_number,
        predicted_last_page_items_number,
        actual_last_page_items_number,
        max_items_on_page,
    )


def item_pages_are_full_except_last_assert(
    self,
    total_items_number,
    predicted_last_page_items_number,
    actual_last_page_items_number,
    max_items_on_page,
):
    if max_items_on_page >= 12:
        assert (
            item_page_find_how_many_items_for_sale_max(self) == total_items_number
            and predicted_last_page_items_number == actual_last_page_items_number
        )
    else:
        assert item_page_find_how_many_items_for_sale_max(
            self
        ) == item_page_find_all_items_for_sale(self)
