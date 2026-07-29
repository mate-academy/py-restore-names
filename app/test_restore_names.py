from app.restore_names import restore_names


def test_when_first_name_equal_to_none() -> None:
    user = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]

    restore_names(user)

    assert user == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]


def test_without_first_name() -> None:
    user = [{
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]

    restore_names(user)

    assert user == [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
