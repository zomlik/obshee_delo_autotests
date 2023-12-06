import pytest
from pages.donation_obshee_delo.main_page import MainPage
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


class TestPayment(FakeData):
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

