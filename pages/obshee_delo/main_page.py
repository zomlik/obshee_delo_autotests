from base.seleniumbase import BasePage
from pages.obshee_delo.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def logo_is_visible(self):
        return self.is_visible(MainPageLocators.LOGO)

    def help_payment_button_is_visible(self):
        return self.is_visible(MainPageLocators.HELP_PAYMENT_BUTTON)

    def help_payment_button_click(self):
        return self.is_clicable(MainPageLocators.HELP_PAYMENT_BUTTON).click()

    def content_is_visible(self):
        return self.all_elems_is_visible(MainPageLocators.CONTENT)

