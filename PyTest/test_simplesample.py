from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Firts approach: using functions
def test_setup():
    global driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.maximize_window()

def test_login():
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.find_element(by=By.NAME, value='username').send_keys('Admin' + Keys.ESCAPE)
    driver.find_element(by=By.NAME, value='password').send_keys('admin123' + Keys.ESCAPE)
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()
    assert driver.title == 'OrangeHRM'

def test_logout():
    driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i').click()
    driver.find_element(by=By.LINK_TEXT, value='Logout').click()

def test_teardown():
    driver.close()
    driver.quit()

