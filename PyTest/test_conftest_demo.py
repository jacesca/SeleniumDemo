import allure
import pytest
import moment

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures('test_setup')
class TestSample():
    def test_login(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        driver.find_element(by=By.NAME, value='username').send_keys('Admin' + Keys.ESCAPE)
        driver.find_element(by=By.NAME, value='password').send_keys('admin123' + Keys.ESCAPE)
        driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
        assert driver.title == 'OrangeHRM'

    def test_logout(self):
        try:
            driver = self.driver
            driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i').click()
            driver.find_element(by=By.LINK_TEXT, value='Logout').click()
            assert driver.title == 'abc'

        except AssertionError as error:
            print('Assertion error occurred!')
            print(error)
            allure.attach(
                self.driver.get_screenshot_as_png(),
                name='screenshot'+moment.now().strftime('%Y-%m-%d_%H-%M-%S-%f'),
                attachment_type=allure.attachment_type.PNG
            )
            raise

        except Exception as error:
            print('There was an exception!')
            print(error)
            raise

        else:
            print('No exception occurred!')

        finally:
            print('test_logout completed!')




