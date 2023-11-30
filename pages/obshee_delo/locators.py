from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGO = (By.CSS_SELECTOR, ".logo")
    HELP_PAYMENT_BUTTON = (By.CSS_SELECTOR, ".slogan_wrap_text")
    CONTENT = (By.CSS_SELECTOR, ".cmsms_post_cont")
