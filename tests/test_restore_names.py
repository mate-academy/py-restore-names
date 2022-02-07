import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_users",
    [
        [
            [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"last_name": "Adams",
              "full_name": "Mike Adams"}],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}]
        ]
    ]
)
def test_update_of_none_or_missing_value(users, expected_users):
    restore_names(users)
    assert users == expected_users


@pytest.mark.parametrize(
    "users, expected_users",
    [
        [
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}]
        ]
    ]
)
def test_do_nothing_if_value_is_correct(users, expected_users):
    restore_names(users)
    assert users == expected_users

