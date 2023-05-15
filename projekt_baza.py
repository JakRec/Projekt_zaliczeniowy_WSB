# projekt bedzie opieral sie o testowanie funkcjonalnosci strony magento.softwaretestingboard.com/

# wczytanie bibliotek
import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
driver.get("https://magento.softwaretestingboard.com/")
sleep(5)
