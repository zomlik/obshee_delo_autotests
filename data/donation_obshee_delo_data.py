from locators.donation_obshee_delo_locators import MainPageLocators


class DataMenu:
    base_url = "https://donation.obshee-delo.ru/"
    main = f"{base_url}#glavnaya"
    new_cartoon = f"{base_url}#uchastie"
    cost_project = f"{base_url}#pervaya_seriya"
    about = f"{base_url}#obshee-delo"

    data = [(MainPageLocators.MENU_MAIN, main),
            (MainPageLocators.MENU_SUPPORT_NEW_CARTON, new_cartoon),
            (MainPageLocators.MENU_COST_PROJECT, cost_project),
            (MainPageLocators.MENU_ABOUT, about)
            ]


