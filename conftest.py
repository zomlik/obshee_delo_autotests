import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def options():
    options = Options()
    options.add_argument("log-level=3")
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--headless")
    return options


@pytest.fixture(scope="function")
def browser(options):
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(10)
    yield browser
    browser.quit()
