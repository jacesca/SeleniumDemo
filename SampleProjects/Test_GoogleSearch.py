import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class GoogleSearchTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        cls.driver.implicitly_wait(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ESCAPE)
        self.driver.find_element(by=By.NAME, value='btnK').click()
        self.assertEqual(self.driver.title, 'Automation step by step - Buscar con Google')

    def test_search_jacesca(self):
        self.driver.get("https://google.com")
        self.driver.find_element(by=By.NAME, value='q').send_keys('Jacesca' + Keys.ESCAPE)
        self.driver.find_element(by=By.NAME, value='btnK1').click()
        self.assertEqual(self.driver.title, 'Jacesca - Buscar con Google')


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='../Reports'))

