
from app import restore_names


def test_restore_names() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]

    result = restore_names.restore_names(users)

    assert result is None

    assert users == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith",
        },
    ]
