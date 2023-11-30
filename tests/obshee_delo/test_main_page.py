from pages.obshee_delo.main_page import MainPage

URL = "https://общее-дело.рф/"


def test_logo(browser):
    page = MainPage(browser)
    page.open(URL)
    page.logo_is_visible()


def test_help_payment_button(browser):
    page = MainPage(browser)
    page.open(URL)
    page.help_payment_button_is_visible()


def test_content(browser):
    page = MainPage(browser)
    page.open(URL)
    page.content_is_visible()