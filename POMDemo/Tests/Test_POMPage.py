import unittest
import HtmlTestRunner

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
# Inside the Selenium/POMDemo/Tests folder:
#     python Test_POMPage.py
# Inside the Selenium folder
#     python -m POMDemo.Tests.Test_POMPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from POMDemo.Pages.HomePage import HomePage
from POMDemo.Pages.LoginPage import LoginPage

class POMPagesTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.username = 'Admin'
        cls.password = 'admin123'

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_login_valid(self):
        # Load the page
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        login = LoginPage(self.driver)
        login.enter_username(self.username)
        login.enter_password(self.password)
        login.click_login()

    def test_logout_allowed(self):
        homepage = HomePage(self.driver)
        homepage.click_welcomename()
        homepage.click_logout()

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../../Reports'))

