import time

import pytest
from pages.donation_obshee_delo.main_page import MainPage
from locators.donation_obshee_delo_locators import MainPageLocators
from data.donation_obshee_delo_data import DataMenu
from data.fake_data import FakeData

URL = "https://donation.obshee-delo.ru"


class TestMainPage:
    @pytest.mark.parametrize("locator_button, expected_link", DataMenu.data)
    def test_menu_buttons(self, browser, locator_button, expected_link):
        """Тест проверяет работу кнопок главного меню"""
        page = MainPage(browser)
        page.open(URL)
        page.is_clicable(locator_button).click()
        assert page.current_url() == expected_link

    @pytest.mark.parametrize("buttons", MainPageLocators.list_button_support)
    def test_support_buttons(self, browser, buttons):
        """Тест проверяет что все кнопки ПОДДЕРЖАТЬ работают"""
        page = MainPage(browser)
        page.open(URL)
        page.is_clicable(buttons).click()
        assert page.is_visible(MainPageLocators.PAY_BUTTON)

    def test_payment_form_placeholder(self, browser):
        """Тест проверяет placeholder у формы оплаты"""
        page = MainPage(browser)
        page.open(URL)
        page.menu_support_button_click()
        assert page.get_attribute(MainPageLocators.SUM_FIELD, "placeholder") == "Сумма"
        assert page.get_attribute(MainPageLocators.NAME_FIELD, "placeholder") == "ФИО"
        assert page.get_attribute(MainPageLocators.PHONE_FIELD, "placeholder") == "Телефон"
        assert page.get_attribute(MainPageLocators.EMAIL_FIELD, "placeholder") == "E-mail"


class TestPayment(FakeData):
    def test_min_support_amount(self, browser):
        """Тест проверяет что минемальная сумма перевода не может быть меньше 10 рублей"""
        page = MainPage(browser)
        page.open(URL)
        page.menu_support_button_click()
        page.send_sum(amount=9)
        page.click_pay_button()
        assert page.get_text(locator=MainPageLocators.SUM_ERROR) == "Сумма должна быть больше 10 Руб."

    def test_sum_field_empty(self, browser):
        """Тест проверяет, что невозможно выполнить платеж с пустым полем сумма"""
        page = MainPage(browser)
        page.open(URL)
        page.menu_support_button_click()
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.send_email_field(self.email())
        page.click_pay_button()
        assert page.get_text(MainPageLocators.SUM_ERROR) == "Введите корректную сумму"

    def test_send_support_default(self, browser):
        """Тест проверяет возможность выполнить перевод по банковской карте"""
        page = MainPage(browser)
        page.open(URL)
        page.menu_support_button_click()
        page.send_sum(self.amount(min_value=10, max_value=99999))
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.send_email_field(self.email())
        page.click_pay_button()
        page.click_bank_card()
        page.swith_windows()
        page.leave_iframe()
        assert page.yoomoney_button_pay()

