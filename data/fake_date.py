from random import randint
from faker import Faker


class FakeDate:
    @staticmethod
    def amount(min_value: int, max_value: int):
        return randint(min_value, max_value)

    @property
    def name(self):
        return Faker("ru_RU").name

    @property
    def phone(self):
        return Faker("ru_RU").phone_number

    @property
    def email(self):
        return Faker("ru_RU").email

