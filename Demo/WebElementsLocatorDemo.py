from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

print('***Starting...***')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://google.com")

# Elements can be found by ID, NAME, CLASS_NAME, CSS_SELECTOR, TAG_NAME, LINK_TEXT,
# PARTIAL_LINK_TEXT, XPATH (for XPATH you need an extension in the browser (ChroPath)
# find_element() --> Find one, find_elements() --> Find all