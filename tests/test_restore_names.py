from app.restore_names import restore_names


def test_empty_users():
    assert not restore_names([])


def test_unmatched_first_name():
    tested_user = {
        'full_name': 'full name',
        'first_name': 'full',
        'second_name': 'name'
    }
    losted_user = {
        'second_name': tested_user['second_name'],
        'full_name': tested_user['full_name'],
    }
    restore_names([losted_user])
    assert losted_user == tested_user


def test_none_first_name():
    tested_user = {
        'full_name': 'full name',
        'first_name': 'full',
        'second_name': 'name'
    }
    losted_user = {
        'second_name': tested_user['second_name'],
        'full_name': tested_user['full_name'],
        'first_name': None
    }
    restore_names([losted_user])
    assert losted_user == tested_user
