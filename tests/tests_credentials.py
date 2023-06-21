# essential credentials for tests

from faker import Faker

fake = Faker(locale="pl_PL")

# randomly generated credentials for creating new account tests


def test_firstname():
    return fake.first_name()


def test_surname():
    return fake.last_name()


def test_mail():
    return fake.email()


# not random, valid credentials


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
    elif type == "ok different":
        return "BardzoMocneHaslo3212.a"


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
        return "New York"
    elif credential_type == "postal_code":
        return "12345"
    elif credential_type == "country":
        return "United States"
