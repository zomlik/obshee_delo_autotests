from pages.obshee_delo.payment_page import PaymentPage
from data.fake_data import FakeData


URL = "https://поддержи.общее-дело.рф/"


class TestPayment(FakeData):
    def test_send_support_default(self, browser):
        page = PaymentPage(browser)
        page.open(URL)
        page.click_support_button()
        page.send_sum_field(self.amount(min_value=10, max_value=30000))
        page.send_email_field(self.email())
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.click_donate_button()
        page.swith_iframe_form()
        page.check_pay_button()

    def test_send_support_recurring(self, browser):
        page = PaymentPage(browser)
        page.open(URL)
        page.click_support_button()
        page.select_recurring_payment()
        page.click_sum_500()
        page.send_email_field(self.email())
        page.send_name_field(self.name())
        page.send_phone_field(self.phone())
        page.click_donate_button()
        page.swith_iframe_form()
        page.check_pay_button()

