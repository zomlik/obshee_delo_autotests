import pytest

from pages.poznavalov.main_page import MainPage
from locators.poznovalov_locators import MainPageLocators
from data.fake_date import FakeDate
import time

URL = "https://poznavalov.ru/"


class TestPayment(FakeDate):
    def test_payment_default(self, browser):
        page = MainPage(browser)
        page.open(URL)
        page.click_support_button()
        page.sum_field(self.amount(min_value=10, max_value=30000))
        page.email_field(self.email())
        page.name_field(self.name())
        page.phone_field(self.phone())
        page.click_donate_button()
        page.swith_pay_form_iframe()
        assert page.click_pay_button()

    def test_one_time_support(self, browser):
        page = MainPage(browser)
        page.open(URL)
        page.click_support_button()
        page.click_once_time_button()
        page.sum_field(self.amount(min_value=10, max_value=30000))
        page.email_field(self.email())
        page.name_field(self.name())
        page.phone_field(self.phone())
        page.click_donate_button()
        page.swith_pay_form_iframe()
        assert page.click_pay_button()

