from base.seleniumbase import BasePage
from data.fake_data import FakeData
from locators.donation_obshee_delo_locators import MainPageLocators


class MainPage(BasePage, FakeData):
    def __init__(self, browser):
        super().__init__(browser)

    def click_menu_support_button(self):
        return self.clicable(MainPageLocators.MENU_SUPPORT_BUTTON).click()

    def send_sum(self, amount: int):
        return self.clear_and_send(el=self.visible(MainPageLocators.SUM_FIELD), val=amount)

    def send_sum_500(self):
        return self.visible(MainPageLocators.SUM_500).click()

    def personal_information(self):
        self.visible(MainPageLocators.NAME_FIELD).send_keys(self.name())
        self.visible(MainPageLocators.PHONE_FIELD).send_keys(self.phone())
        self.visible(MainPageLocators.EMAIL_FIELD).send_keys(self.email())

    def send_name_field(self, name: str):
        return self.visible(MainPageLocators.NAME_FIELD).send_keys(name)

    def send_phone_field(self, phone: str):
        return self.visible(MainPageLocators.PHONE_FIELD).send_keys(phone)

    def send_email_field(self, email: str):
        return self.visible(MainPageLocators.EMAIL_FIELD).send_keys(email)

    def click_agree_personal_data(self):
        return self.visible(MainPageLocators.AGREE_PERSONAL_DATA).click()

    def click_donate_button(self):
        return self.clicable(MainPageLocators.DONATE_BUTTON).click()

    def click_bank_card(self):
        return self.clicable(MainPageLocators.BANK_CARD).click()

    def yoomoney_page_pay(self):
        expire = self.credit_card_expire()
        self.visible(MainPageLocators.CREDIT_CARD_FIELD).send_keys(self.credit_card())
        self.visible(MainPageLocators.EXPIRY_MONTH_FIELD).send_keys(expire[:2])
        self.visible(MainPageLocators.EXPIRY_YEAR_FIELD).send_keys(expire[2:])
        self.visible(MainPageLocators.SECURITY_CODE_FIELD).send_keys(self.credit_card_code())
        self.clicable(MainPageLocators.PAY_BUTTON_YOOMONEY).click()
