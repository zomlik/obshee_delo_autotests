from pages.obshee_delo.main_page import MainPage
from locators.obshee_delo_locators import MainPageLocators
from data.fake_data import FakeData

URL = "https://общее-дело.рф/#wysija"


class TestMainPage(FakeData):
    def test_subscription_success(self, browser):
        page = MainPage(browser)
        page.open(URL)
        page.is_visible(MainPageLocators.BANNER_BLOCK)
        page.subscription_field(self.email())
        page.click_subscription_button()
        assert page.get_text(MainPageLocators.SUBSCRIPTION_SUCCESS) == ("Проверьте Ваш почтовый "
                                                                        "ящик и подтвердите свою подписку.")

    def test_subscription_empty_field(self, browser):
        page = MainPage(browser)
        page.open(URL)
        page.is_visible(MainPageLocators.BANNER_BLOCK)
        page.click_subscription_button()
        assert page.get_text(MainPageLocators.SUBSCRIPTION_ERROR) == ("* Необходимо заполнить\n"
                                                                      "* Неверный формат email")

    def test_content_is_visible(self, browser):
        page = MainPage(browser)
        page.open(URL)
        page.content_is_visible()

    def test_click_suppurt_button(self, browser):
        page = MainPage(browser)
        page.open(URL)
        page.click_support_button()
        page.swith_windows()
        assert page.current_url() == "https://xn--d1aadek5agm.xn----9sbkcac6brh7h.xn--p1ai/"


