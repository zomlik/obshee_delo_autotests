from selenium.webdriver.common.by import By


class CloudPaymentsLocators:
    """Страница оплаты CloudPayments"""
    CARD_FIELD = (By.CSS_SELECTOR, "#card")
    CARD_DATA_FIELD = (By.CSS_SELECTOR, "#date")
    CARD_CVV_FIELD = (By.CSS_SELECTOR, "#cvv")
    PAY_BUTTON = (By.CSS_SELECTOR, ".button.button_primary")
    PAY_MESSAGE = (By.CSS_SELECTOR, ".text.h4")


class UKassaLocators:
    """Страница оплаты Юкасса"""
    BANK_CARD = (By.CSS_SELECTOR, ".mui-1khahxm.eqnn621")
    CREDIT_CARD_FIELD = (By.XPATH, "//input[@name='card-number']")
    EXPIRY_MONTH_FIELD = (By.XPATH, "//input[@name='expiry-month']")
    EXPIRY_YEAR_FIELD = (By.XPATH, "//input[@name='expiry-year']")
    SECURITY_CODE_FIELD = (By.XPATH, "//input[@name='security-code']")
    YOOMONEY_PAY_MESSAGE = (By.CSS_SELECTOR, ".qa-informer-title")
    PAY_BUTTON_YOOMONEY = (By.CSS_SELECTOR, ".mui-75qv9u.e1ai9pc90")
    SWITH_IFRAME_LOCATOR = (By.CSS_SELECTOR, "iframe")
