from string import ascii_lowercase
from random import randint, choices


from app.restore_names import restore_names


def create_random_user():
    first_name = ''.join(choices(
        ascii_lowercase,
        k=randint(2, 50),
    ))
    second_name = ''.join(choices(
        ascii_lowercase,
        k=randint(2, 50),
    ))
    full_name = first_name + ' ' + second_name

    return {
        'full_name': full_name,
        'second_name': second_name,
        'first_name': first_name,
    }


def test_empty_users():
    assert not restore_names([])


def test_unmatched_first_name():
    tested_user = create_random_user()
    losted_user = {
        'second_name': tested_user['second_name'],
        'full_name': tested_user['full_name'],
    }
    restore_names([losted_user])
    assert losted_user == tested_user


def test_none_first_name():
    tested_user = create_random_user()
    losted_user = {
        'second_name': tested_user['second_name'],
        'full_name': tested_user['full_name'],
        'first_name': None
    }
    restore_names([losted_user])
    assert losted_user == tested_user
