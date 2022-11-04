# -*- coding: utf-8 -*-
# Taken from Katalon
# Steps: 1. Click on Katalon extension in chrome
#        2. Add a new TestSuites
#        3. Start the record
#        4. Make all the actions you need
#        5. Stop the record
#        6. Explore all the elements saved and review the identification method (id, name, css, xpath)
#        7. Click on export and select python code
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest, time, re


class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.google.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(by=By.NAME, value="username").click()
        driver.find_element(by=By.NAME, value="username").clear()
        driver.find_element(by=By.NAME, value="username").send_keys("Admin")
        driver.find_element(by=By.NAME, value="password").click()
        driver.find_element(by=By.NAME, value="password").clear()
        driver.find_element(by=By.NAME, value="password").send_keys("admin123")
        driver.find_element(by=By.XPATH, value="//button[@type='submit']").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
        driver.find_element(by=By.XPATH, value="//div[@id='app']/div/div/header/div/div[2]/ul/li/span/p").click()
        driver.find_element(by=By.LINK_TEXT, value="Logout").click()
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
