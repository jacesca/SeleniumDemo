import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from POMDemo.Pages.HomePage import HomePage
from POMDemo.Pages.LoginPage import LoginPage

# Definint the parameters
USERNAME = 'Admin'
PASSWORD = 'admin123'

# Configuring the driver
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

# Loading the page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Loging in
login = LoginPage(driver)
login.enter_username(USERNAME)
login.enter_password(PASSWORD)
login.click_login()

# Loging out
homepage = HomePage(driver)
homepage.click_welcomename()
homepage.click_logout()

time.sleep(5)
print(driver.title)

driver.close()
driver.quit()