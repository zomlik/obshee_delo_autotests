from base.seleniumbase import BasePage
from data.fake_data import FakeData
from locators.obshee_delo_locators import PaymentPageLocators
from locators.payment_system_locators import CloudPaymentsLocators


class PaymentPage(BasePage, FakeData):

    def click_support_button(self):
        return self.to_be_clickable(PaymentPageLocators.SUPPORT_BUTTON).click()

    def select_recurring_payment(self):
        return self.to_be_clickable(PaymentPageLocators.RECURRING_PAYMENT).click()

    def click_sum_500(self):
        return self.to_be_clickable(PaymentPageLocators.SUM_500).click()

    def send_sum_field(self, amount: int):
        return self.clear_and_send(el=self.visibility_of_element(PaymentPageLocators.SUM_FIELD), val=amount)

    def send_email_field(self, email: str):
        return self.visibility_of_element(PaymentPageLocators.EMAIL_FIELD).send_keys(email)

    def send_name_field(self, name: str):
        return self.visibility_of_element(PaymentPageLocators.NAME_FIELD).send_keys(name)

    def send_phone_field(self, phone: str):
        return self.visibility_of_element(PaymentPageLocators.PHONE_FIELD).send_keys(phone)

    def click_donate_button(self):
        return self.to_be_clickable(PaymentPageLocators.DONATE_BUTTON).click()

    def swith_iframe_form(self):
        return self.swith_iframe(PaymentPageLocators.IFRAME)

    def cloudpayments_page(self):
        self.visibility_of_element(CloudPaymentsLocators.CARD_FIELD).send_keys(self.credit_card_number())
        self.visibility_of_element(CloudPaymentsLocators.CARD_DATA_FIELD).send_keys(self.credit_card_expire())
        self.visibility_of_element(CloudPaymentsLocators.CARD_CVV_FIELD).send_keys(self.credit_card_cvv())
        self.to_be_clickable(CloudPaymentsLocators.PAY_BUTTON).click()
