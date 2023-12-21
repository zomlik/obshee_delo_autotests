from base.seleniumbase import BasePage
from locators.obshee_delo_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_subscribe_button(self):
        return self.visible(MainPageLocators.SUBSCRIPTION_BUTTON).click()

    def send_subscribe_field(self, email: str):
        return self.visible(MainPageLocators.SUBSCRIPTION_FIELD).send_keys(email)

    def click_support_button(self):
        return self.clicable(MainPageLocators.HELP_PAYMENT_BUTTON).click()

    def content_is_visible(self):
        return self.all_elems_is_visible(MainPageLocators.CONTENT)

