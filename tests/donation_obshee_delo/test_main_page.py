from pages.donation_obshee_delo.main_page import MainPage
from locators.donation_obshee_delo_locators import MainPageLocators
from data.fake_data import FakeData
import time

URL = "https://donation.obshee-delo.ru"


def test_click_on_button_payment(browser):
    page = MainPage(browser)
    page.open(URL)
    page.header_support_button_click()
    page.send_sum(9)
    page.click_pay_button()
    assert page.error_message_sum() == "Сумма должна быть больше 10 Руб."


def test_send_support_default(browser):
    """Тест проверяет возможность выполнить перевод по банковской карте"""
    page = MainPage(browser)
    page.open(URL)
    page.header_support_button_click()
    page.send_sum(FakeData.sum)
    page.send_name_field(FakeData.name)
    page.send_phone_field(FakeData.phone)
    page.send_email_field(FakeData.email)
    page.click_pay_button()
    page.click_bank_card()
    page.swith_windows()
    page.leave_iframe()
    assert page.yoomoney_button_pay()

