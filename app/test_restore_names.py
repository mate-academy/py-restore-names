import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
        ),
        (
            [
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                }
            ],
            [
                {
                    "first_name": "Anna",
                    "last_name": "Smith",
                    "full_name": "Anna Smith",
                }
            ],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Brown",
                    "full_name": "John Brown",
                },
                {
                    "last_name": "White",
                    "full_name": "Kate White",
                },
                {
                    "first_name": "Bob",
                    "last_name": "Green",
                    "full_name": "Bob Green",
                },
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Brown",
                    "full_name": "John Brown",
                },
                {
                    "first_name": "Kate",
                    "last_name": "White",
                    "full_name": "Kate White",
                },
                {
                    "first_name": "Bob",
                    "last_name": "Green",
                    "full_name": "Bob Green",
                },
            ],
        ),
        (
            [],
            [],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "Mary Jane Smith",
                }
            ],
            [
                {
                    "first_name": "Mary",
                    "last_name": "Smith",
                    "full_name": "Mary Jane Smith",
                }
            ],
        ),
    ]
)
def test_restore_names_expected_results(
    users: list[dict],
    expected: list[dict]
) -> None:
    restore_names(users)
    assert users == expected


def test_restore_names_returns_none() -> None:
    users = [
        {
            "first_name": None,
            "full_name": "Alice Cooper",
        }
    ]

    result = restore_names(users)

    assert result is None


def test_restore_names_modifies_original_dictionary() -> None:
    user = {
        "first_name": None,
        "full_name": "David Miller",
    }
    users = [user]

    restore_names(users)

    assert users[0] is user
    assert user["first_name"] == "David"


def test_restore_names_preserves_existing_first_name() -> None:
    users = [
        {
            "first_name": "Alex",
            "full_name": "Alexander Johnson",
        }
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Alex"


def test_restore_names_preserves_other_fields() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Wilson",
            "full_name": "Emma Wilson",
            "age": 25,
            "city": "London",
        }
    ]

    restore_names(users)

    assert users[0] == {
        "first_name": "Emma",
        "last_name": "Wilson",
        "full_name": "Emma Wilson",
        "age": 25,
        "city": "London",
    }
