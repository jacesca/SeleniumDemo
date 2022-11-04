import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
  parser.addoption('--browser', action='store', default='chrome',
                   help='Type in browser name. chrome or firefox only.')

@pytest.fixture(scope="class")
def test_setup(request):
    # To run from command line:
    #   pytest test_conftest_demo.py --browser firefox
    # or
    #   pytest test_conftest_demo.py --browser chrome

    browser = request.config.getoption('--browser')
    if browser == 'chrome':
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == 'firefox':
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    else:
        driver = None
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
    driver.quit()