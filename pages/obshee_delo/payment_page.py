from base.seleniumbase import BasePage
from locators.obshee_delo_locators import PaymentPageLocators


class PaymentPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)

    def click_support_button(self):
        return self.clicable(PaymentPageLocators.SUPPORT_BUTTON).click()

    def select_recurring_payment(self):
        return self.clicable(PaymentPageLocators.RECURRING_PAYMENT).click()

    def click_sum_500(self):
        return self.clicable(PaymentPageLocators.SUM_500).click()

    def send_sum_field(self, amount: int):
        return self.clear_and_send(el=self.visible(PaymentPageLocators.SUM_FIELD), val=amount)

    def send_email_field(self, email: str):
        return self.visible(PaymentPageLocators.EMAIL_FIELD).send_keys(email)

    def send_name_field(self, name: str):
        return self.visible(PaymentPageLocators.NAME_FIELD).send_keys(name)

    def send_phone_field(self, phone: str):
        return self.visible(PaymentPageLocators.PHONE_FIELD).send_keys(phone)

    def click_donate_button(self):
        return self.clicable(PaymentPageLocators.DONATE_BUTTON).click()

    def swith_iframe_form(self):
        return self.swith_iframe(PaymentPageLocators.IFRAME)

    def check_pay_button(self):
        return self.visible(PaymentPageLocators.PAY_BUTTON_FORM)
