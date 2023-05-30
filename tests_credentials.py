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


def test_password(type):
    if type == "no special char":
        return "aaaaaaaa"
    elif type == "only two special chars":
        return "aaaaaa1A"
    elif type == "weak":
        return "aaaaa1A."
    elif type == "medium":
        return "aaaaa1A.:"
    elif type == "strong":
        return "aaaaa1A.:aa"
    elif type == "very strong":
        return "aaaaa1A.:aaa!"
    elif type == "ok":
        return "BardzoMocneHaslo3212."


"""
def test_password_no_special_char():
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
"""


def account_data_valid(credential_type):
    if credential_type == "name":
        return "John"
    elif credential_type == "surname":
        return "Doe"
    elif credential_type == "mail":
        return "johndoe@xyb.com"
    elif credential_type == "password":
        return "ndeNZ.eJN5kEGdp"
    elif credential_type == "phone":
        return "123456789"
    elif credential_type == "company":
        return "BestCompany Ltd"
    elif credential_type == "adress":
        return "Long Street 123"
    elif credential_type == "city":
        return "London"
    elif credential_type == "postal_code":
        return "12345"
    elif credential_type == "country":
        return "United States"
