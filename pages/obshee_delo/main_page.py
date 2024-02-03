from base.seleniumbase import BasePage
from locators.obshee_delo_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_subscribe_button(self):
        return self.visibility_of_element(MainPageLocators.SUBSCRIPTION_BUTTON).click()

    def send_subscribe_field(self, email: str):
        return self.visibility_of_element(MainPageLocators.SUBSCRIPTION_FIELD).send_keys(email)

    def click_support_button(self):
        return self.to_be_clickable(MainPageLocators.HELP_PAYMENT_BUTTON).click()

    def content_is_visible(self):
        return self.visibility_of_all_elements(MainPageLocators.CONTENT)

