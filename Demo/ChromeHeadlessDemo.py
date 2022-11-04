import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# The Headless mode is a feature which allows the execution of a full version of the
# Chrome Browser. It provides the ability to control Chrome via external programs.
# The headless mode can run on servers without the need for dedicated display or graphics.
# List of Chrome Driver command line arguments
# -- https://gist.github.com/ntamvl/4f93bbb7c9b4829c601104a2d2f91fe5
# -- https://gist.github.com/ntamvl/4f93bbb7c9b4829c601104a2d2f91fe5#file-list-of-chrome-driver-command-line-arguments-md


print('***Starting (headless mode)...***')

chrome_options = Options()
chrome_options.headless = True
chrome_options.add_argument('--disable-extensions')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get("https://google.com")

print(driver.title)
driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ENTER)
print(driver.title)
#print(driver.page_source)

driver.close()
driver.quit()

print('***Test Completed!***')
