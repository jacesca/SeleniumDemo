import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class LoginLogoutTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_login_valid(self):
        # Load the page
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        # Write the username
        self.driver.find_element(by=By.NAME, value='username').send_keys('Admin' + Keys.ESCAPE)
        # Write the pwd
        self.driver.find_element(by=By.NAME, value='password').send_keys('admin123' + Keys.ESCAPE)
        # Click on Login Button
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

    def test_logout_allowed(self):
        # Click on the user welcome name
        self.driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i').click()
        # Click on logout
        self.driver.find_element(by=By.LINK_TEXT, value='Logout').click()
        # driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../../Reports'))

