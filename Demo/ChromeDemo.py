import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

print('***Starting...***')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.set_page_load_timeout(10)
driver.get("https://google.com")

# Inspect the page and look for the name of the object you need
# # First method: 1. Write what you are looking for and press Escape key.
# #               2. Wait until search button is activated.
# #               3. Click on search button
# driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ESCAPE)
# time.sleep(1)
# driver.find_element(by=By.NAME, value='btnK').click()
# time.sleep(2)
# driver.close()
# driver.quit()

# Second method: 1. Write what you are looking for and press enter.
driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ENTER)
time.sleep(2)
driver.close()
driver.quit()

# # Third method: 1. Write what you are looking for and press Escape key.
# #               2. Wait until search button is activated.
# #               3. Click on search button
# driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step' + Keys.ESCAPE)
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'btnK'))).click()
# time.sleep(2)
# driver.close()
# driver.quit()

# # Fourth method: 1. Write what you are looking for.
# #                2. Click on search button
# driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step')
# time.sleep(2)
# driver.find_element(by=By.NAME, value='btnK').send_keys(Keys.ENTER)
# time.sleep(2)
# driver.close()
# driver.quit()

# # Fifth method: 1. Write what you are looking for.
# #               2. Click on search button
# driver.find_element(by=By.NAME, value='q').send_keys('Automation step by step')
# WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.NAME, 'btnK'))).send_keys(Keys.ENTER)
# time.sleep(2)
# driver.close()
# driver.quit()

print('***Task Completed!***')

# # Selenium - wait until element is present, visible and interactable
# # 1. If your usecase is to validate the presence of any element you need to induce
# #    WebDriverWait setting the expected_conditions as presence_of_element_located()
# #    which is the expectation for checking that an element is present on the DOM of
# #    a page. This does not necessarily mean that the element is visible. So the effective
# #    line of code will be:
# WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".reply-button"))).click()
#
# # 2. If your usecase is to extract any attribute of any element you need to induce WebDriverWait
# #    setting the expected_conditions as visibility_of_element_located(locator) which is an expectation
# #    for checking that an element is present on the DOM of a page and visible. Visibility means that
# #    the element is not only displayed but also has a height and width that is greater than 0.
# #    So in your usecase effectively the line of code will be:
# email = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "element_css"))).get_attribute("value")
#
# # 3. If your usecase is to invoke click() on any element you need to induce WebDriverWait setting
# #    the expected_conditions as element_to_be_clickable() which is an expectation for for
# #    checking an element is visible and enabled such that you can click it. So in your usecase
# #    effectively the line of code will be:
# WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".reply-button"))).click()
#
# # Source: https://stackoverflow.com/questions/59130200/selenium-wait-until-element-is-present-visible-and-interactable
# # webdriver_manager: https://github.com/SergeyPirogov/webdriver_manager
