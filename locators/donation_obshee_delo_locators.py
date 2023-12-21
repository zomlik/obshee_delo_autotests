from selenium.webdriver.common.by import By


class MainPageLocators:
    """Главное меню"""
    MENU_MAIN = (By.CSS_SELECTOR, "#u84-4")
    MENU_SUPPORT_NEW_CARTON = (By.CSS_SELECTOR, "#u98-6")
    MENU_COST_PROJECT = (By.CSS_SELECTOR, "#u89-4")
    MENU_ABOUT = (By.CSS_SELECTOR, "#u104-6")
    MENU_SUPPORT_BUTTON = (By.CSS_SELECTOR, ".header-support__btn")
    LIST_OF_MENU_BUTTONS = [MENU_MAIN, MENU_SUPPORT_NEW_CARTON, MENU_COST_PROJECT, MENU_ABOUT]

    """Форма оплаты на сайте donation.obshee-delo"""
    SUM_500 = (By.XPATH, "//div[@data-value='500']")
    SUM_FIELD = (By.CSS_SELECTOR, ".donate_amount_flex")
    NAME_FIELD = (By.XPATH, "//input[@name='leyka_donor_name']")
    PHONE_FIELD = (By.XPATH, "//input[@name='leyka_mobilnyy-telefon']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='leyka_donor_email']")
    AGREE_PERSONAL_DATA = (By.XPATH, "//div/span/label[2]")
    BANK_CARD = (By.CSS_SELECTOR, ".mui-1khahxm.eqnn621")

    DONATE_BUTTON = (By.CSS_SELECTOR, ".leyka-default-submit")

    """Страница оплаты на сайте Юкасса"""
    CREDIT_CARD_FIELD = (By.XPATH, "//input[@name='card-number']")
    EXPIRY_MONTH_FIELD = (By.XPATH, "//input[@name='expiry-month']")
    EXPIRY_YEAR_FIELD = (By.XPATH, "//input[@name='expiry-year']")
    SECURITY_CODE_FIELD = (By.XPATH, "//input[@name='security-code']")
    YOOMONEY_PAY_MESSAGE = (By.CSS_SELECTOR, ".qa-informer-title")
    PAY_BUTTON_YOOMONEY = (By.CSS_SELECTOR, ".mui-75qv9u.e1ai9pc90")
    SWITH_IFRAME_LOCATOR = (By.CSS_SELECTOR, "iframe")

