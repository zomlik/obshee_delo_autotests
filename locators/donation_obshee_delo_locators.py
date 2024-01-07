from selenium.webdriver.common.by import By


class MainPageLocators:
    """Главное меню Donation Obshee-Delo"""
    MENU_SUPPORT_BUTTON = (By.CSS_SELECTOR, ".header-support__btn")

    """Форма оплаты Donation Obshee-Delo"""
    SUM_FIELD = (By.CSS_SELECTOR, ".donate_amount_flex")
    NAME_FIELD = (By.XPATH, "//input[@name='leyka_donor_name']")
    PHONE_FIELD = (By.XPATH, "//input[@name='leyka_mobilnyy-telefon']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='leyka_donor_email']")
    AGREE_PERSONAL_DATA = (By.XPATH, "//div/span/label[2]")

    DONATE_BUTTON = (By.CSS_SELECTOR, ".leyka-default-submit")
