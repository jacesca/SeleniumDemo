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

driver.get("https://google.com")
driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ESCAPE)
driver.find_element(by=By.NAME, value='btnK').click()
print(driver.title)

driver.close()
driver.quit()