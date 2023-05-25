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


def test_password_no_special_char():
    return "aaaaaaaa"


def test_password_only_two_special_chars():
    return "aaaaaa1A"


def test_password_ok_weak():
    return "aaaaa1A."


def test_password_ok_medium():
    return "aaaaa1A.:"


def test_password_ok_strong():
    return "aaaaa1A.:aa"


def test_password_ok_very_strong():
    return "aaaaa1A.:aaa!"
