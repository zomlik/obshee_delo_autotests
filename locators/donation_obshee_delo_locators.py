from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_SUPPORT_BUTTON = (By.CSS_SELECTOR, "#u2521-4")

    SUM_FIELD = (By.CSS_SELECTOR, "#inMoney")
    NAME_FIELD = (By.CSS_SELECTOR, "#CustName")
    PHONE_FIELD = (By.CSS_SELECTOR, "#cps_phone")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#cps_email")
    PAY_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary.btn-sm.btnfull")
    BANK_CARD = (By.XPATH, "//img[@alt='logo_cards']")

    SUM_ERROR = (By.CSS_SELECTOR, "#inMoney-error")
    NAME_FIELD_ERROR = (By.CSS_SELECTOR, "#CustName-error")
    PHONE_FIELD_ERROR = ()
    EMAIL_FIELD_ERROR = (By.CSS_SELECTOR, "#cps_email-error")

    PAY_BUTTON_YOOMONEY = (By.CSS_SELECTOR, ".mui-75qv9u.e1ai9pc90")
    SWITH_LOCATOR = (By.CSS_SELECTOR, "iframe")
