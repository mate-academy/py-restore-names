from app.restore_names import restore_names


def test_restore_names_with_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ], "First name should be restored from full_name"


def test_restore_names_without_first_name_field() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ], "First name should be restored from full_name when the field is missing"


def test_no_change_when_first_name_exists() -> None:
    users = [
        {
            "first_name": "Emily",
            "last_name": "Clark",
            "full_name": "Emily Clark",
        }
    ]

    restore_names(users)

    assert users == [
        {
            "first_name": "Emily",
            "last_name": "Clark",
            "full_name": "Emily Clark",
        }
    ], "First name should not change if it already exists"


def test_empty_user_list() -> None:
    users = []

    restore_names(users)

    assert users == [], "Empty list should remain empty"
