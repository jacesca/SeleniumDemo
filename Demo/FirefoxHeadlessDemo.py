import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


print('***Starting (headless mode)...***')

browser_options = Options()
browser_options.headless = True
browser_options.add_argument('--disable-extensions') # More options: https://www.browserstack.com/docs/automate/selenium/firefox-profile#python

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=browser_options)
driver.get("https://google.com")
print(driver.title)

driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ENTER)
time.sleep(2)
print(driver.title)

driver.close()
driver.quit()

print('***Test Completed!***')