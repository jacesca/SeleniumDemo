import unittest
import HtmlTestRunner

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class TestSeleniumDemoErr(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        options = webdriver.ChromeOptions()
        #options.add_experimental_option('excludeSwitches', ['enable-logging'])

        cls.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        cls.driver.implicitly_wait(10)
        cls.driver.set_page_load_timeout(10)
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()

    def test_search_1(self):
        self.driver.get("https://google.com")
        self.driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ENTER)
        self.assertEqual(self.driver.title, 'Automation step by step - Buscar con Google')


    def test_search_2(self):
        self.driver.get("https://google.com")
        self.driver.find_element(by=By.NAME, value='q').send_keys('Raghav Pal' + Keys.ENTER)
        self.assertEqual(self.driver.title, 'Raghav Pal- Buscar con Google')

    @unittest.skip
    def test_search_skip(self):
        self.driver.get("https://google.com")
        self.driver.find_element(by=By.NAME, value='q').send_keys('python install html test runner' + Keys.ENTER)
        self.assertEqual(self.driver.title, 'python install html test runner - Buscar con Google')

if __name__ == '__main__':
    # unittest.main(verbosity=2)
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/jaces/Documents/certificate/Courses/Selenium/Reports', verbosity=2))
