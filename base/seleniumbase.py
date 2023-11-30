from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    TIMEOUT = 15

    def __init__(self, browser):
        self.browser = browser

    def open(self, url: str):
        return self.browser.get(url)

    def is_visible(self, locator: tuple, timeout: int = TIMEOUT):
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator))

    def all_elems_is_visible(self, locator: tuple, timeout: int = TIMEOUT):
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator))
