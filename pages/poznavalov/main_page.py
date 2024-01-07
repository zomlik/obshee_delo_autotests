from base.seleniumbase import BasePage
from locators.poznovalov_locators import MainPageLocators
from locators.payment_system_locators import CloudPaymentsLocators
from data.fake_data import FakeData


class MainPage(BasePage, FakeData):

    def __init__(self, browser):
        super().__init__(browser)

    def click_support_button(self):
        return self.to_be_clickable(MainPageLocators.HEADER_SUPPORT_BUTTON).click()

    def click_once_time_button(self):
        return self.to_be_clickable(MainPageLocators.ONE_SUPPORT).click()

    def sum_field(self, amount: int):
        return self.clear_and_send(el=self.visibility_of_element(MainPageLocators.SUM_FIELD), val=amount)

    def send_email_field(self, email: str):
        return self.visibility_of_element(MainPageLocators.EMAIL_FIELD).send_keys(email)

    def send_name_field(self, name: str):
        return self.visibility_of_element(MainPageLocators.NAME_FIELD).send_keys(name)

    def send_phone_field(self, phone:str):
        return self.visibility_of_element(MainPageLocators.PHONE_FIELD).send_keys(phone)

    def click_donate_button(self):
        return self.to_be_clickable(MainPageLocators.DONATE_BUTTON).click()

    def cloudpayments_page(self):
        self.visibility_of_element(CloudPaymentsLocators.CARD_FIELD).send_keys(self.credit_card_number())
        self.visibility_of_element(CloudPaymentsLocators.CARD_DATA_FIELD).send_keys(self.credit_card_expire())
        self.visibility_of_element(CloudPaymentsLocators.CARD_CVV_FIELD).send_keys(self.credit_card_cvv())
        self.to_be_clickable(CloudPaymentsLocators.PAY_BUTTON).click()

    def swith_payment_form_iframe(self):
        return self.swith_iframe(locator=MainPageLocators.IFRAME)
