from random import choice, randint
from string import ascii_letters
from mimesis import Person, Gender


def random_string(start: int = 1, end: int = 15) -> str:
    return ''.join(choice(ascii_letters) for _ in range(randint(start, end)))


def email_generator() -> str:
    """
    Generates random email
    Example: random_data@domain.com
    :return:
    """
    person = Person()
    domains = ['yandex.ru', 'gmail.com', 'yahoo.go', 'apple.com']
    random_email = person.email(domains=domains)

    return random_email


def full_name_generator() -> str:
    person = Person()
    full_name = person.full_name(Gender.FEMALE)

    return full_name
