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


def goto_main_page(self):
    driver = self.driver
    driver.get(self.locators.main_page_adress)


def sign_in_page_sign_in_button_click(self):
    driver = self.driver
    driver.find_element(By.XPATH, '//*[@id="send2"]/span').click()


def login_to_account(self):
    driver = self.driver
    goto_main_page(self)
    print(
        driver.find_element(By.XPATH, self.locators.main_page_welcome_message_id).text
    )
    if (
        driver.find_element(By.XPATH, self.locators.main_page_welcome_message_id).text
        == "Welcome, John Doe!"
    ):
        print("Użytkownik zalogowany, kontynuacja")
    else:
        print("Użytkownik niezalogowany, logowanie")
        driver.find_element(By.XPATH, self.locators.main_page_sign_in_button_id).click()
        driver.find_element(By.XPATH, self.locators.sign_in_page_mail_id).send_keys(
            self.dane.account_data_valid("mail")
        )
        driver.find_element(By.XPATH, self.locators.sign_in_page_password_id).send_keys(
            self.dane.account_data_valid("password")
        )
        sign_in_page_sign_in_button_click(self)
    sleep(2)


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
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[2]/span/button"
        ).click()
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[2]/div/ul/li[1]/a"
        ).click()
        el1 = driver.find_element(
            By.XPATH,
            '//*[@id="maincontent"]/div[2]/div[1]/div[3]/div[2]/div[1]/div[1]/p',
        ).text
        assert el1 == self.dane.account_data_valid(
            "name"
        ) + " " + self.dane.account_data_valid(
            "surname"
        ) + "\n" + self.dane.account_data_valid(
            "mail"
        )

    def test_delivery_adress_no_firstname(self):
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        driver.find_element(By.XPATH, '//*[@id="firstname"]').clear()
        driver.find_element(By.XPATH, '//*[@id="telephone"]').send_keys(
            self.dane.account_data_valid("phone")
        )
        driver.find_element(By.XPATH, '//*[@id="street_1"]').send_keys(
            self.dane.account_data_valid("adress")
        )
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(
            self.dane.account_data_valid("city")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="region_id"]')
        ).select_by_visible_text("Arizona")
        driver.find_element(By.XPATH, '//*[@id="zip"]').send_keys(
            self.dane.account_data_valid("postal_code")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="country"]')
        ).select_by_visible_text(self.dane.account_data_valid("country"))
        driver.find_element(By.XPATH, '//*[@title="Save Address"]').click()
        sleep(1)
        assert driver.find_element(By.XPATH, '//*[@id="firstname-error"]')

    def test_delivery_adress_no_lastname(self):
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        driver.find_element(By.XPATH, '//*[@id="lastname"]').clear()
        driver.find_element(By.XPATH, '//*[@id="telephone"]').send_keys(
            self.dane.account_data_valid("phone")
        )
        driver.find_element(By.XPATH, '//*[@id="street_1"]').send_keys(
            self.dane.account_data_valid("adress")
        )
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(
            self.dane.account_data_valid("city")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="region_id"]')
        ).select_by_visible_text("Arizona")
        driver.find_element(By.XPATH, '//*[@id="zip"]').send_keys(
            self.dane.account_data_valid("postal_code")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="country"]')
        ).select_by_visible_text(self.dane.account_data_valid("country"))
        driver.find_element(By.XPATH, '//*[@title="Save Address"]').click()
        sleep(1)
        assert driver.find_element(By.XPATH, '//*[@id="lastname-error"]')

    def test_delivery_adress_no_phone_number(self):
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        driver.find_element(By.XPATH, '//*[@id="street_1"]').send_keys(
            self.dane.account_data_valid("adress")
        )
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(
            self.dane.account_data_valid("city")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="region_id"]')
        ).select_by_visible_text("Arizona")
        driver.find_element(By.XPATH, '//*[@id="zip"]').send_keys(
            self.dane.account_data_valid("postal_code")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="country"]')
        ).select_by_visible_text(self.dane.account_data_valid("country"))
        driver.find_element(By.XPATH, '//*[@title="Save Address"]').click()
        sleep(1)
        assert driver.find_element(By.XPATH, '//*[@id="telephone-error"]')

    def test_delivery_adress_no_adress(self):
        # error occurs only with no input in first row
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        driver.find_element(By.XPATH, '//*[@id="telephone"]').send_keys(
            self.dane.account_data_valid("phone")
        )
        driver.find_element(By.XPATH, '//*[@id="city"]').send_keys(
            self.dane.account_data_valid("city")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="region_id"]')
        ).select_by_visible_text("Arizona")
        driver.find_element(By.XPATH, '//*[@id="zip"]').send_keys(
            self.dane.account_data_valid("postal_code")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="country"]')
        ).select_by_visible_text(self.dane.account_data_valid("country"))
        driver.find_element(By.XPATH, '//*[@title="Save Address"]').click()
        sleep(1)
        assert driver.find_element(By.XPATH, '//*[@id="street_1-error"]')

    def test_delivery_adress_no_city(self):
        driver = self.driver
        login_to_account(self)
        goto_account_data(self)
        goto_shipping_adress_page(self)
        driver.find_element(By.XPATH, '//*[@id="street_1"]').send_keys(
            self.dane.account_data_valid("adress")
        )
        driver.find_element(By.XPATH, '//*[@id="telephone"]').send_keys(
            self.dane.account_data_valid("phone")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="region_id"]')
        ).select_by_visible_text("Arizona")
        driver.find_element(By.XPATH, '//*[@id="zip"]').send_keys(
            self.dane.account_data_valid("postal_code")
        )
        Select(
            driver.find_element(By.XPATH, '//*[@id="country"]')
        ).select_by_visible_text(self.dane.account_data_valid("country"))
        driver.find_element(By.XPATH, '//*[@title="Save Address"]').click()
        sleep(1)
        assert driver.find_element(By.XPATH, '//*[@id="city-error"]')

    def test_cart_adding(self):
        driver = self.driver
        login_to_account(self)
        sleep(2)
        driver.find_element(By.XPATH, '//*[@class="action showcart"]').click()
        sleep(1)
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
        driver.find_element(
            By.XPATH, '//*[@id="option-label-size-143-item-166"]'
        ).click()
        driver.find_element(
            By.XPATH, '//*[@id="option-label-color-93-item-50"]'
        ).click()
        driver.find_element(
            By.XPATH,
            '//*[@id="maincontent"]/div[3]/div/div[2]/div[3]/div/div/ol/li[1]/div/div/div[4]/div/div[1]/form/button',
        ).click()
        sleep(3)
        print(
            driver.find_element(
                By.XPATH,
                "/html/body/div[1]/header/div[2]/div[1]/a/span[2]/span[1]",
            ).text
        )
        assert (
            int(
                driver.find_element(
                    By.XPATH, "/html/body/div[1]/header/div[2]/div[1]/a/span[2]/span[1]"
                ).text
            )
            == 1
        )


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)
