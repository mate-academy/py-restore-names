import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        # Сценарій 1: first_name дорівнює None
        (
            [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"}],

            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"}]
        ),
        # Сценарій 2: Ключ first_name відсутній
        (
            [{"last_name": "Adams",
              "full_name": "Mike Adams"}],

            [{"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}]
        )
    ]
)
def test_restore_names_functionality(users: list,
                                     expected_users: list) -> None:
    restore_names(users)
    assert users == expected_users
