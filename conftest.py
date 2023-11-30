import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="session")
def options():
    options = Options()
    #options.add_argument("--headless")
    return options


@pytest.fixture(scope="session")
def browser(options):
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()