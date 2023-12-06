from selenium.webdriver.common.by import By


class MainPageLocators:
    """Главная страница"""
    SUPPORT_BUTTON_1 = (By.CSS_SELECTOR, "#u2069-2")
    SUPPORT_BUTTON_2 = (By.CSS_SELECTOR, "#u2433-2")
    SUPPORT_BUTTON_3 = (By.CSS_SELECTOR, "#u2650-2")
    SUPPORT_BUTTON_4 = (By.CSS_SELECTOR, "#u2638-2")
    SUPPORT_BUTTON_5 = (By.CSS_SELECTOR, "#u2641-2")
    SUPPORT_BUTTON_6 = (By.CSS_SELECTOR, "#u2647-2")
    SUPPORT_BUTTON_7 = (By.CSS_SELECTOR, "#u2069-2")
    list_button_support = [SUPPORT_BUTTON_1, SUPPORT_BUTTON_2, SUPPORT_BUTTON_3,
                           SUPPORT_BUTTON_4, SUPPORT_BUTTON_5, SUPPORT_BUTTON_6,
                           SUPPORT_BUTTON_7
                           ]

    """Главное меню"""
    MENU_MAIN = (By.CSS_SELECTOR, "#u84-4")
    MENU_SUPPORT_NEW_CARTON = (By.CSS_SELECTOR, "#u98-6")
    MENU_COST_PROJECT = (By.CSS_SELECTOR, "#u89-4")
    MENU_ABOUT = (By.CSS_SELECTOR, "#u104-6")
    MENU_SUPPORT_BUTTON = (By.CSS_SELECTOR, "#u2521-4")
    LIST_OF_MENU_BUTTONS = [MENU_MAIN, MENU_SUPPORT_NEW_CARTON, MENU_COST_PROJECT, MENU_ABOUT]

    """Форма оплаты на сайте donation.obshee-delo"""
    SUM_FIELD = (By.CSS_SELECTOR, "#inMoney")
    NAME_FIELD = (By.CSS_SELECTOR, "#CustName")
    PHONE_FIELD = (By.CSS_SELECTOR, "#cps_phone")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#cps_email")
    BANK_CARD = (By.XPATH, "//img[@alt='logo_cards']")

    PAY_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-sm.btnfull")

    SUM_ERROR = (By.CSS_SELECTOR, "#inMoney-error")
    NAME_FIELD_ERROR = (By.CSS_SELECTOR, "#CustName-error")
    PHONE_FIELD_ERROR = ()
    EMAIL_FIELD_ERROR = (By.CSS_SELECTOR, "#cps_email-error")

    """Страница оплаты на сайте Юкасса"""
    PAY_BUTTON_YOOMONEY = (By.CSS_SELECTOR, ".mui-75qv9u.e1ai9pc90")
    SWITH_IFRAME_LOCATOR = (By.CSS_SELECTOR, "iframe")

