from app.restore_names import restore_names


def test_restore_first_name_when_missing() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restores_first_name_when_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_does_not_restore_first_name_when_it_present() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restores_first_name_when_missing_or_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users)
    for user in users:
        assert user["first_name"] == "Jack"


def test_restore_first_name_from_single_word_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "JackHoly",
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "JackHoly"


def test_does_not_restore_first_name_when_empty() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_restores_first_name_from_extra_spaces_full_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)
    assert users[0]["first_name"] == "Jack"
