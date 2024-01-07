from random import randint
from faker import Faker


class FakeData:
    fake = Faker("ru_RU")

    @staticmethod
    def amount(min_value: int, max_value: int):
        return randint(min_value, max_value)

    @property
    def name(self):
        return self.fake.name

    @property
    def phone(self):
        return self.fake.phone_number

    @property
    def email(self):
        return self.fake.email

    @property
    def credit_card_expire(self):
        return self.fake.credit_card_expire

    @staticmethod
    def credit_card_number():
        return "5106502628283431"

    @staticmethod
    def credit_card_cvv():
        return "456"
