from base.seleniumbase import BasePage
from data.fake_data import FakeData
from locators.donation_obshee_delo_locators import MainPageLocators
from locators.payment_system_locators import UKassaLocators


class MainPage(BasePage, FakeData):
    def __init__(self, browser):
        super().__init__(browser)

    def click_menu_support_button(self):
        return self.to_be_clickable(MainPageLocators.MENU_SUPPORT_BUTTON).click()

    def send_sum(self, amount: int):
        return self.clear_and_send(el=self.visibility_of_element(MainPageLocators.SUM_FIELD), val=amount)

    def send_name_field(self, name: str):
        return self.visibility_of_element(MainPageLocators.NAME_FIELD).send_keys(name)

    def send_phone_field(self, phone: str):
        return self.visibility_of_element(MainPageLocators.PHONE_FIELD).send_keys(phone)

    def send_email_field(self, email: str):
        return self.visibility_of_element(MainPageLocators.EMAIL_FIELD).send_keys(email)

    def click_agree_personal_data(self):
        return self.visibility_of_element(MainPageLocators.AGREE_PERSONAL_DATA).click()

    def click_donate_button(self):
        return self.to_be_clickable(MainPageLocators.DONATE_BUTTON).click()

    def click_bank_card(self):
        return self.to_be_clickable(UKassaLocators.BANK_CARD).click()

    def yoomoney_payment_page(self):
        card_month_expire = self.credit_card_expire()[:2]
        card_year_expire = self.credit_card_expire()[2:]
        self.visibility_of_element(UKassaLocators.CREDIT_CARD_FIELD).send_keys(self.credit_card_number())
        self.visibility_of_element(UKassaLocators.EXPIRY_MONTH_FIELD).send_keys(card_month_expire)
        self.visibility_of_element(UKassaLocators.EXPIRY_YEAR_FIELD).send_keys(card_year_expire)
        self.visibility_of_element(UKassaLocators.SECURITY_CODE_FIELD).send_keys(self.credit_card_cvv())
        self.to_be_clickable(UKassaLocators.PAY_BUTTON_YOOMONEY).click()
