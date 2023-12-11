from base.seleniumbase import BasePage
from locators.obshee_delo_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def subscription_field(self, email: str):
        return self.is_located(MainPageLocators.SUBSCRIPTION_FIELD).send_keys(email)

    def click_subscription_button(self):
        return self.is_clicable(MainPageLocators.SUBSCRIPTION_BUTTON).click()

    def click_support_button(self):
        return self.is_clicable(MainPageLocators.HELP_PAYMENT_BUTTON).click()

    def content_is_visible(self):
        return self.all_elems_is_visible(MainPageLocators.CONTENT)

