import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.maximize_window()

# Load the page
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

# Write the username
driver.find_element(by=By.NAME, value='username').send_keys('Admin' + Keys.ESCAPE)

# Write the pwd
driver.find_element(by=By.NAME, value='password').send_keys('admin123' + Keys.ESCAPE)

# Click on Login Button
driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button').click()

# Click on the user welcome name
driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div[1]/div[2]/ul/li/span/i').click()

# Click on logout
driver.find_element(by=By.LINK_TEXT, value='Logout').click()
#driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[1]/div[1]/header/div[1]/div[2]/ul/li/ul/li[4]/a').click()

time.sleep(5)

print(driver.title)

driver.close()
driver.quit()