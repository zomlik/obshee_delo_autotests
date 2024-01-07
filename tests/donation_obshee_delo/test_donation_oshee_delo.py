from pages.donation_obshee_delo.main_page import MainPage
from locators.donation_obshee_delo_locators import MainPageLocators
from locators.payment_system_locators import UKassaLocators
from data.fake_data import FakeData
from data.urls import URL


class TestPayment(FakeData):
    def test_aree_personal_data_is_disabled(self, browser):
        page = MainPage(browser)
        page.open(URL.DONATION_OBSHEE_DELO)
        page.click_menu_support_button()
        page.send_sum(self.amount(min_value=10, max_value=30000))
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.send_email_field(self.email())
        assert page.visibility_of_element(MainPageLocators.DONATE_BUTTON).is_enabled() is False

    def test_send_support_default(self, browser):
        page = MainPage(browser)
        page.open(URL.DONATION_OBSHEE_DELO)
        page.click_menu_support_button()
        page.send_sum(self.amount(min_value=10, max_value=30000))
        page.send_email_field(self.email())
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.click_agree_personal_data()
        page.click_donate_button()
        page.click_bank_card()
        page.yoomoney_payment_page()
        assert page.get_text(UKassaLocators.YOOMONEY_PAY_MESSAGE) == "Не сработало"
