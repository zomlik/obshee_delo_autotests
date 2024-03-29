from pages.obshee_delo.main_page import MainPage
from locators.obshee_delo_locators import MainPageLocators
from data.fake_data import FakeData
from data.urls import URL


class TestMainPage(FakeData):
    def test_subscribe_empty_field(self, browser):
        page = MainPage(browser)
        page.open(URL.OBSHEE_DELO)
        page.click_subscribe_button()
        page.click_subscribe_button()
        assert page.get_text(MainPageLocators.SUBSCRIPTION_ERROR) == "* Необходимо заполнить\n* Неверный формат email"

    def test_wrong_email(self, browser):
        page = MainPage(browser)
        page.open(URL.OBSHEE_DELO)
        page.click_subscribe_button()
        page.send_subscribe_field("emal@")
        page.click_subscribe_button()
        assert page.get_text(MainPageLocators.SUBSCRIPTION_ERROR) == "* Неверный формат email"

    def test_subscribe_success(self, browser):
        page = MainPage(browser)
        page.open(URL.OBSHEE_DELO)
        page.click_subscribe_button()
        page.send_subscribe_field(self.email())
        page.click_subscribe_button()
        assert page.get_text(MainPageLocators.SUBSCRIPTION_SUCCESS) == "Проверьте Ваш почтовый ящик и подтвердите свою подписку."

    def test_content_is_visible(self, browser):
        page = MainPage(browser)
        page.open(URL.OBSHEE_DELO)
        page.content_is_visible()

    def test_click_suppurt_button(self, browser):
        page = MainPage(browser)
        page.open(URL.OBSHEE_DELO)
        page.click_support_button()
        page.swith_windows()
        assert page.current_url() == "https://xn--d1aadek5agm.xn----9sbkcac6brh7h.xn--p1ai/"
