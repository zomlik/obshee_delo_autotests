from base.seleniumbase import BasePage
from data.fake_data import FakeData
from locators.donation_obshee_delo_locators import MainPageLocators


class MainPage(BasePage, FakeData):
    def __init__(self, browser):
        super().__init__(browser)

    def menu_support_button_click(self):
        return self.is_clicable(MainPageLocators.MENU_SUPPORT_BUTTON).click()

    def send_sum(self, amount: int):
        return self.is_visible(MainPageLocators.SUM_FIELD).send_keys(amount)

    def send_name_field(self, name: str):
        return self.is_visible(MainPageLocators.NAME_FIELD).send_keys(name)

    def send_phone_field(self, phone: str):
        return self.is_visible(MainPageLocators.PHONE_FIELD).send_keys(phone)

    def send_email_field(self, email: str):
        return self.is_visible(MainPageLocators.EMAIL_FIELD).send_keys(email)

    def click_pay_button(self):
        return self.is_clicable(MainPageLocators.PAY_BUTTON).click()

    def click_bank_card(self):
        return self.is_clicable(MainPageLocators.BANK_CARD).click()

    def yoomoney_button_pay(self):
        return self.is_clicable(MainPageLocators.PAY_BUTTON_YOOMONEY)
