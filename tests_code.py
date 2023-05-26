# projekt bedzie opieral sie o testowanie funkcjonalnosci strony magento.softwaretestingboard.com/ z wykrozystaniem biblioteki selenium

# wczytanie bibliotek
import unittest
from selenium import webdriver

# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from time import sleep
import testing_data


def login_to_account(self):
    driver = self.driver
    driver.get("https://magento.softwaretestingboard.com/")
    driver.find_element(
        By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[2]/a"
    ).click()
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(
        self.dane.account_data_valid("mail")
    )
    driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(
        self.dane.account_data_valid("password")
    )
    driver.find_element(By.XPATH, '//*[@id="send2"]/span').click()
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


class TestClass(unittest.TestCase):
    driver = webdriver.Chrome()

    def setUp(self):
        # self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 2)
        self.driver.implicitly_wait(5)
        self.dane = testing_data

    def test_website_opening(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        assert driver.title == "Home Page"

    def test_creating_account_no_name(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys(
            self.dane.test_mail()
        )
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(
            self.dane.test_password()
        )
        driver.find_element(By.XPATH, '//input[@id="password-confirmation"]').send_keys(
            self.dane.test_password()
        )
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button'
        ).click()
        assert (
            driver.find_element(By.XPATH, '//*[@id="firstname-error"]').get_attribute(
                "generated"
            )
            == "true"
        )

    def test_creating_account_no_surname(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys(
            self.dane.test_mail()
        )
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(
            self.dane.test_password()
        )
        driver.find_element(By.XPATH, '//input[@id="password-confirmation"]').send_keys(
            self.dane.test_password()
        )
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button'
        ).click()
        assert (
            driver.find_element(By.XPATH, '//*[@id="lastname-error"]').get_attribute(
                "generated"
            )
            == "true"
        )

    def test_ceating_account_no_mail(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(
            self.dane.test_surname()
        )
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(
            self.dane.test_password()
        )
        driver.find_element(By.XPATH, '//input[@id="password-confirmation"]').send_keys(
            self.dane.test_password()
        )
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button'
        ).click()
        assert (
            driver.find_element(
                By.XPATH, '//*[@id="email_address-error"]'
            ).get_attribute("generated")
            == "true"
        )

    def test_creating_account_password_to_short(self):
        driver = self.driver
        wait = self.wait
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(
            self.dane.test_surname()
        )
        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys(
            self.dane.test_mail()
        )
        for password_length in range(7):
            driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("a")
            sleep(0.5)
            password_length += 1
            if (
                driver.find_element(By.XPATH, '//*[@id="password-error"]').text
                == "Minimum length of this field must be equal or greater than 8 symbols. Leading and trailing spaces will be ignored."
            ):
                continue
            else:
                assert False
        assert True

    def test_creating_account_password_no_special_char(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(
            self.dane.test_surname()
        )
        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys(
            self.dane.test_mail()
        )
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys("aaaaaaaa")
        sleep(2)
        assert (
            driver.find_element(By.XPATH, '//*[@id="password-error"]').text
            == "Minimum of different classes of characters in password is 3. Classes of characters: Lower Case, Upper Case, Digits, Special Characters."
        )

    def test_creating_account_password_not_match(self):
        driver = self.driver
        wait = self.wait
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(
            self.dane.test_surname()
        )
        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys(
            self.dane.test_mail()
        )
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(
            self.dane.test_password()
        )
        driver.find_element(By.XPATH, '//*[@id="password-confirmation"]').send_keys(
            self.dane.test_password() + "a"
        )
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button'
        ).click()
        sleep(2)
        assert (
            driver.find_element(By.XPATH, '//*[@id="password-confirmation-error"]').text
            == "Please enter the same value again."
        )

    def test_creating_account_password_weak(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(
            self.dane.test_surname()
        )
        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys(
            self.dane.test_mail()
        )
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(
            self.dane.test_password_ok_weak()
        )
        sleep(2)
        assert (
            driver.find_element(
                By.XPATH, '//*[@id="password-strength-meter-label"]'
            ).text
            == "Weak"
        )

    def test_creating_account_password_medium(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(
            self.dane.test_surname()
        )
        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys(
            self.dane.test_mail()
        )
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(
            self.dane.test_password_ok_medium()
        )
        sleep(2)
        assert (
            driver.find_element(
                By.XPATH, '//*[@id="password-strength-meter-label"]'
            ).text
            == "Medium"
        )

    def test_creating_account_password_strong(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(
            self.dane.test_surname()
        )
        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys(
            self.dane.test_mail()
        )
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(
            self.dane.test_password_ok_strong()
        )
        sleep(2)
        assert (
            driver.find_element(
                By.XPATH, '//*[@id="password-strength-meter-label"]'
            ).text
            == "Strong"
        )

    def test_creating_account_password_very_strong(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        ).click()
        driver.find_element(By.XPATH, '//input[@id="firstname"]').send_keys(
            self.dane.test_firstname()
        )
        driver.find_element(By.XPATH, '//input[@id="lastname"]').send_keys(
            self.dane.test_surname()
        )
        driver.find_element(By.XPATH, '//input[@id="email_address"]').send_keys(
            self.dane.test_mail()
        )
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(
            self.dane.test_password_ok_very_strong()
        )
        self.wait_5s
        assert (
            driver.find_element(
                By.XPATH, '//*[@id="password-strength-meter-label"]'
            ).text
            == "Very Strong"
        )

    def test_login_to_existing_account(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[2]/a"
        ).click()
        driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(
            self.dane.account_data_valid("mail")
        )
        driver.find_element(By.XPATH, '//*[@id="pass"]').send_keys(
            self.dane.account_data_valid("password")
        )
        driver.find_element(By.XPATH, '//*[@id="send2"]/span').click()
        sleep(4)

        assert (
            driver.find_element(
                By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[1]/span"
            ).text
            == "Welcome, "
            + self.dane.account_data_valid("name")
            + " "
            + self.dane.account_data_valid("surname")
            + "!"
        )

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


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main(verbosity=2)


"""    def test_ceating_account_positive(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        el1 = driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        )
        el1.click()
        el2 = driver.find_element(By.XPATH, '//input[@id="firstname"]')
        el2.send_keys("John")
        el3 = driver.find_element(By.XPATH, '//input[@id="lastname"]')
        el3.send_keys("Doe")
        el4 = driver.find_element(By.XPATH, '//input[@id="email_address"]')
        el4.send_keys("johndoe@xye.com")
        driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(
            "VeryDifficultPassword123"
        )
        driver.find_element(By.XPATH, '//input[@id="password-confirmation"]').send_keys(
            "VeryDifficultPassword123"
        )
        driver.find_element(
            By.XPATH, '//*[@id="form-validate"]/div/div[1]/button'
        ).click()
        assert driver.find_element(
            By.XPATH,
            '//div[@data-bind="html: $parent.prepareMessageForHtml(message.text)"]',
        )
"""
