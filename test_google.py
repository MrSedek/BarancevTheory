# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re, pytest


class GoogleCom(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_google_com(self):
        driver = self.driver
        driver.get("https://www.google.com/")
        driver.find_element_by_name("q").clear()
        driver.find_element_by_name("q").send_keys("test")
        driver.find_element_by_name("q").send_keys(Keys.ENTER)
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='Все результаты'])[3]/following::h3[1]").click()



if __name__ == "__main__":
    unittest.main()
