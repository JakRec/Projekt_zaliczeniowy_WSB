from faker import Faker

fake = Faker(locale="pl_PL")

# print(fake.first_name())
# print(fake.last_name())
# print(fake.email())


def test_firstname():
    return fake.first_name()


def test_surname():
    return fake.last_name()


def test_mail():
    return fake.email()


def test_password():
    return "BardzoMocneHaslo3212."
