import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.microsoft import EdgeChromiumDriverManager

print('***Starting...***')
# Work in headless mood.

driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=browser_options)
driver.get("https://google.com")
print(driver.title)

driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ENTER)
time.sleep(2)
print(driver.title)

driver.close()
driver.quit()

print('***Test Completed!***')