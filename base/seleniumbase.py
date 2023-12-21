from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver import ActionChains


class BasePage:
    TIMEOUT = 15

    def __init__(self, browser):
        self.browser = browser

    def current_url(self) -> None:
        return self.browser.current_url

    def open(self, url: str) -> None:
        return self.browser.get(url)

    def get_text(self, locator) -> str:
        return self.visible(locator).text

    def get_attribute(self, locator: tuple, attribute: str) -> str:
        return self.visible(locator).get_attribute(attribute)

    def clear_and_send(self, el: WebElement, val) -> None:
        el.clear()
        el.send_keys(val)

    def visible(self, locator: tuple, timeout: int = TIMEOUT) -> WebElement:
        return wait(self.browser, timeout).until(EC.visibility_of_element_located(locator),
                                                 message=f"Can't find element by locator {locator}")

    def clicable(self, locator: tuple, timeout: int = TIMEOUT) -> WebElement:
        return wait(self.browser, timeout).until(EC.element_to_be_clickable(locator),
                                                 message=f"Can't find or click on element by locator {locator}")

    def all_elems_is_visible(self, locator: tuple, timeout: int = TIMEOUT) -> list[WebElement]:
        return wait(self.browser, timeout).until(EC.visibility_of_all_elements_located(locator),
                                                 message=f"Can't find elements by locator {locator}")

    def swith_iframe(self, locator: tuple) -> None:
        iframe = self.browser.find_element(*locator)
        self.browser.switch_to.frame(iframe)

    def leave_iframe(self) -> None:
        return self.browser.switch_to.default_content()

    def current_windows(self) -> None:
        return self.browser.current_window_handle

    def swith_windows(self) -> None:
        for window_handle in self.browser.window_handles:
            if window_handle != self.current_windows():
                self.browser.switch_to.window(window_handle)
                break
