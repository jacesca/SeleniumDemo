from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from POMDemo.Locators.Locators import Locators

class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.username_textbox_name = Locators.username_textbox_name
        self.password_textbox_name = Locators.password_textbox_name
        self.login_button_xpath = Locators.login_button_xpath

    def enter_username(self, username):
        self.driver.find_element(by=By.NAME, value=self.username_textbox_name).clear()
        self.driver.find_element(by=By.NAME, value=self.username_textbox_name).send_keys(username + Keys.ESCAPE)

    def enter_password(self, password):
        self.driver.find_element(by=By.NAME, value=self.password_textbox_name).clear()
        self.driver.find_element(by=By.NAME, value=self.password_textbox_name).send_keys(password + Keys.ESCAPE)

    def click_login(self):
        self.driver.find_element(by=By.XPATH, value=self.login_button_xpath).click()

