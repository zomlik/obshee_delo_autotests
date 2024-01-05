from locators.payment_system_locators import CloudPaymentsLocators
from locators.poznovalov_locators import MainPageLocators
from pages.poznavalov.main_page import MainPage
from data.fake_data import FakeData
from data.urls import URL


class TestPayment(FakeData):
    def test_min_sum_payment(self, browser):
        page = MainPage(browser)
        page.open(URL.POZNAVALOV)
        page.click_support_button()
        page.sum_field(amount=9)
        page.send_name_field(self.name())
        page.send_email_field(self.email())
        page.send_phone_field(self.phone())
        page.click_donate_button()
        assert page.get_text(MainPageLocators.ERROR_MESSAGE) == "УКАЗАННЫЙ РАЗМЕР СЛИШКОМ МАЛ (ДОПУСТИМО МИНИМУМ 10 ₽)"

    def test_payment_default(self, browser):
        page = MainPage(browser)
        page.open(URL.POZNAVALOV)
        page.click_support_button()
        page.sum_field(self.amount(min_value=10, max_value=30000))
        page.send_email_field(self.email())
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.click_donate_button()
        page.swith_payment_form_iframe()
        page.cloudpayments_page()
        assert page.get_text(CloudPaymentsLocators.PAY_MESSAGE) == "Операция не может быть обработана"

    def test_one_time_support(self, browser):
        page = MainPage(browser)
        page.open(URL.POZNAVALOV)
        page.click_support_button()
        page.click_once_time_button()
        page.sum_field(self.amount(min_value=10, max_value=30000))
        page.send_email_field(self.email())
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.click_donate_button()
        page.swith_payment_form_iframe()
        page.cloudpayments_page()
        assert page.get_text(CloudPaymentsLocators.PAY_MESSAGE) == "Операция не может быть обработана"
