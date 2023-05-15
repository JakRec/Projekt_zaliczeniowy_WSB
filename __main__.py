# projekt bedzie opieral sie o testowanie funkcjonalnosci strony magento.softwaretestingboard.com/ z wykrozystaniem biblioteki selenium

# wczytanie bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep


class TestClass(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.action = webdriver.ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 5)

    def test_website_opening(self):
        driver = self.driver
        driver.get("https://magento.softwaretestingboard.com/")
        assert driver.title == "Home Page"

    def test_ceating_account(self):
        driver = self.driver
        action = self.action
        wait = self.wait
        driver.get("https://magento.softwaretestingboard.com/")
        el1 = driver.find_element(
            By.XPATH, "/html/body/div[1]/header/div[1]/div/ul/li[3]/a"
        )
        # KLIKANIE ROZWIAZAC
        action.click(el1)
        driver.web
        wait(4)
        assert driver.title == "Create New Customer Account"


def tearDown(self):
    self.driver.close()


if __name__ == "__main__":
    unittest.main()
