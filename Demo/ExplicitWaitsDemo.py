from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get("https://google.com")
driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ESCAPE)

wait = WebDriverWait(driver, 10)
element = wait.until(EC.element_to_be_clickable((By.NAME, 'btnK')))
element.click()
# driver.find_element(by=By.NAME, value='btnK').click()

driver.close()
driver.quit()