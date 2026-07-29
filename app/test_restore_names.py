from app.restore_names import restore_names

user_with_none = [
    {
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    },
]

user_with_missing = [
    {
        "last_name": "Adams",
        "full_name": "Mike Adams",
    },
]


def test_restore_names_with_none_name() -> None:
    restore_names(user_with_none)
    assert user_with_none[0]["first_name"] == "Jack"


def test_restore_names_with_missing_name() -> None:
    restore_names(user_with_missing)
    assert user_with_missing[0]["first_name"] == "Mike"
