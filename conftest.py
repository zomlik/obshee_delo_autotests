import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def options():
    options = Options()
    #options.add_argument("--headless")
    return options


@pytest.fixture(scope="function")
def browser(options):
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    browser.quit()
