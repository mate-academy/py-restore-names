from app.restore_names import restore_names


def test_when_first_name_is_none():
    broken_data = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    corrected_data = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
    ]
    restore_names(broken_data)
    assert broken_data == corrected_data


def test_when_first_name_is_lost():
    broken_data = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    corrected_data = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(broken_data)
    assert broken_data == corrected_data


def test_for_many_users_mixed_errors():
    broken_data = [
        {
            "first_name": None,
            "last_name": "Daniels",
            "full_name": "Jack Daniels",
        },
        {
            "last_name": "Rossum",
            "full_name": "Guido van Rossum",
        },
        {
            "last_name": "Schumacher",
            "full_name": "Michael Schumacher",
        },
        {
            "first_name": "Thomas",
            "last_name": "Anderson",
            "full_name": "Thomas Anderson",
        },
    ]
    corrected_data = [
        {
            "first_name": "Jack",
            "last_name": "Daniels",
            "full_name": "Jack Daniels",
        },
        {
            "first_name": "Guido",
            "last_name": "Rossum",
            "full_name": "Guido van Rossum",
        },
        {
            "first_name": "Michael",
            "last_name": "Schumacher",
            "full_name": "Michael Schumacher",
        },
        {
            "first_name": "Thomas",
            "last_name": "Anderson",
            "full_name": "Thomas Anderson",
        },
    ]
    restore_names(broken_data)
    assert broken_data == corrected_data
