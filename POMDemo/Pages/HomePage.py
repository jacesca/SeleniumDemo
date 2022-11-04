from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from POMDemo.Locators.Locators import Locators


class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.welcome_menu_xpath = Locators.welcome_menu_xpath
        self.logout_menu_linktext = Locators.logout_menu_linktext

    def click_welcomename(self):
        self.driver.find_element(by=By.XPATH, value=self.welcome_menu_xpath).click()

    def click_logout(self):
        self.driver.find_element(by=By.LINK_TEXT, value=self.logout_menu_linktext).click()
