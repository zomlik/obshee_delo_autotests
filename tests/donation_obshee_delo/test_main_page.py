from pages.donation_obshee_delo.main_page import MainPage
from locators.donation_obshee_delo_locators import MainPageLocators
from data.fake_data import FakeData

URL = "https://donation.obshee-delo.ru"


class TestPayment(FakeData):
    def test_min_support_amount_500(self, browser):
        page = MainPage(browser)
        page.open(URL)
        page.click_menu_support_button()
        page.send_sum_500()
        page.personal_information()
        page.click_agree_personal_data()
        page.click_donate_button()
        page.click_bank_card()
        page.yoomoney_page_pay()
        assert page.get_text(MainPageLocators.YOOMONEY_PAY_MESSAGE) == "Не сработало"

    def test_donate_button_is_disabled(self, browser):
        page = MainPage(browser)
        page.open(URL)
        page.click_menu_support_button()
        page.send_sum(self.amount(min_value=10, max_value=30000))
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.send_email_field(self.email())
        assert page.visible(MainPageLocators.DONATE_BUTTON).is_enabled() is False, "Кнопка активна"

    def test_send_support_default(self, browser):
        page = MainPage(browser)
        page.open(URL)
        page.click_menu_support_button()
        page.send_sum(self.amount(min_value=10, max_value=30000))
        page.send_email_field(self.email())
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.click_agree_personal_data()
        page.click_donate_button()
        page.click_bank_card()
        page.yoomoney_page_pay()
        assert page.get_text(MainPageLocators.YOOMONEY_PAY_MESSAGE) == "Не сработало"


