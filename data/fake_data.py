from random import randint
from faker import Faker


class FakeData:
    fake = Faker("ru_RU")

    sum = randint(10, 99999)
    name = fake.name()
    phone = fake.phone_number()
    email = fake.email()
