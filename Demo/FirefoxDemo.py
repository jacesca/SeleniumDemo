import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager

print('***Starting...***')

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://google.com")
print(driver.title)

driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ENTER)
time.sleep(2)
print(driver.title)

driver.close()
driver.quit()

print('***Test Completed!***')