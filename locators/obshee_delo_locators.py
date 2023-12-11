from selenium.webdriver.common.by import By


class MainPageLocators:
    MAIN_LINK_MENU = (By.CSS_SELECTOR, ".menu-item-4588")
    BANNER_BLOCK = (By.CSS_SELECTOR, ".bannerControls")
    SUBSCRIPTION_FIELD = (By.XPATH, "//input[@name='wysija[user][email]']")
    SUBSCRIPTION_BUTTON = (By.CSS_SELECTOR, ".wysija-submit.wysija-submit-field")
    SUBSCRIPTION_ERROR = (By.CSS_SELECTOR, ".formErrorContent")
    SUBSCRIPTION_SUCCESS = (By.CSS_SELECTOR, ".updated>ul>li")
    HELP_PAYMENT_BUTTON = (By.CSS_SELECTOR, ".slogan_wrap_text")
    CONTENT = (By.CSS_SELECTOR, ".cmsms_post_cont")


class PaymentPageLocators:
    IFRAME = (By.CSS_SELECTOR, ".with-appled")

    SUPPORT_BUTTON = (By.CSS_SELECTOR, ".header__button.btn.btn--transparent.js-scroll")

    RECURRING_PAYMENT = (By.XPATH, "//a[@data-periodicity='monthly']")
    SUM_500 = (By.XPATH, "//div[@data-value='500']")
    SUM_FIELD = (By.CSS_SELECTOR, ".donate_amount_flex")
    EMAIL_FIELD = (By.XPATH, "//input[@name='leyka_donor_email']")
    NAME_FIELD = (By.XPATH, "//input[@name='leyka_donor_name']")
    PHONE_FIELD = (By.XPATH, "//input[@name='leyka_mobilnyy-telefon']")

    DONATE_BUTTON = (By.CSS_SELECTOR, ".leyka-default-submit")

    PAY_BUTTON_FORM = (By.CSS_SELECTOR, ".button.button_primary")

