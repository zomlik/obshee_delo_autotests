from random import randint
from faker import Faker


class FakeData:
    LOCALIZATION = "ru_RU"

    @staticmethod
    def amount(min_value: int, max_value: int):
        return randint(min_value, max_value)

    @property
    def name(self):
        return Faker(self.LOCALIZATION).name

    @property
    def phone(self):
        return Faker(self.LOCALIZATION).phone_number

    @property
    def email(self):
        return Faker(self.LOCALIZATION).email

