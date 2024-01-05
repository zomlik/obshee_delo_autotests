from selenium.webdriver.common.by import By


class MainPageLocators:
    """Главное меню Donation Obshee-Delo"""
    MENU_MAIN = (By.CSS_SELECTOR, "#u84-4")
    MENU_SUPPORT_NEW_CARTON = (By.CSS_SELECTOR, "#u98-6")
    MENU_COST_PROJECT = (By.CSS_SELECTOR, "#u89-4")
    MENU_ABOUT = (By.CSS_SELECTOR, "#u104-6")
    MENU_SUPPORT_BUTTON = (By.CSS_SELECTOR, ".header-support__btn")
    LIST_OF_MENU_BUTTONS = [MENU_MAIN, MENU_SUPPORT_NEW_CARTON, MENU_COST_PROJECT, MENU_ABOUT]

    """Форма оплаты Donation Obshee-Delo"""
    SUM_FIELD = (By.CSS_SELECTOR, ".donate_amount_flex")
    NAME_FIELD = (By.XPATH, "//input[@name='leyka_donor_name']")
    PHONE_FIELD = (By.XPATH, "//input[@name='leyka_mobilnyy-telefon']")
    EMAIL_FIELD = (By.XPATH, "//input[@name='leyka_donor_email']")
    AGREE_PERSONAL_DATA = (By.XPATH, "//div/span/label[2]")

    DONATE_BUTTON = (By.CSS_SELECTOR, ".leyka-default-submit")
