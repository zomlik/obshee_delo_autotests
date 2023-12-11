from selenium.webdriver.common.by import By


class MainPageLocators:
    IFRAME = (By.CSS_SELECTOR, ".with-appled")
    HEADER_SUPPORT_BUTTON = (By.CSS_SELECTOR, ".header__panel-support.btn")

    """Форма оплаты"""
    ONE_SUPPORT = (By.XPATH, "//a[@data-periodicity='once']")
    SUM_FIELD = (By.CSS_SELECTOR, ".donate_amount_flex")
    EMAIL_FIELD = (By.XPATH, "//input[@name='leyka_donor_email']")
    NAME_FIELD = (By.XPATH, "//input[@name='leyka_donor_name']")
    PHONE_FIELD = (By.XPATH, "//input[@name='leyka_vash-mobilnyy-telefon']")
    BIRTH_DATE = (By.XPATH, "//input[@name='leyka_data-rozhdeniya']")
    COMMENT_FIELD = (By.XPATH, "//input[@name='leyka_kommentariy']")

    DONATE_BUTTON = (By.CSS_SELECTOR, ".leyka-default-submit")
    PAY_BUTTON = (By.CSS_SELECTOR, ".button.button_primary")
