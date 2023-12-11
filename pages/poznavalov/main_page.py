from base.seleniumbase import BasePage
from locators.poznovalov_locators import MainPageLocators


class MainPage(BasePage):

    def __init__(self, browser):
        super().__init__(browser)

    def click_support_button(self):
        return self.is_clicable(MainPageLocators.HEADER_SUPPORT_BUTTON).click()

    def click_once_time_button(self):
        return self.is_clicable(MainPageLocators.ONE_SUPPORT).click()

    def sum_field(self, amount: int):
        return self.clear_and_send(el=self.is_visible(MainPageLocators.SUM_FIELD), val=amount)

    def send_email_field(self, email: str):
        return self.is_visible(MainPageLocators.EMAIL_FIELD).send_keys(email)

    def send_name_field(self, name: str):
        return self.is_visible(MainPageLocators.NAME_FIELD).send_keys(name)

    def send_phone_field(self, phone:str):
        return self.is_visible(MainPageLocators.PHONE_FIELD).send_keys(phone)

    def click_donate_button(self):
        return self.is_clicable(MainPageLocators.DONATE_BUTTON).click()

    def check_pay_button(self):
        return self.is_visible(MainPageLocators.PAY_BUTTON)

    def swith_pay_form_iframe(self):
        return self.swith_iframe(locator=MainPageLocators.IFRAME)
