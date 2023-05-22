from faker import Faker

fake = Faker()


def test_firstname():
    return "John"


def test_surname():
    return "Doe"


def test_mail():
    return "mail@domain.com"


def test_password():
    return "BardzoMocneHaslo3212."
