import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_data,expected",
    [
        ([{"first_name": None,
           "last_name": "Holy",
           "full_name": "Jack Holy"},
          {"last_name": "Adams",
           "full_name": "Mike Adams"}],
         [{"first_name": "Jack",
           "last_name": "Holy",
           "full_name": "Jack Holy"},
          {"first_name": "Mike",
           "last_name": "Adams",
           "full_name": "Mike Adams"}])
    ],
    ids=[
        "Should restore or add first_name key"
    ]
)
def test_should_restore_names(users_data: list, expected: list) -> None:
    restore_names(users_data)
    assert users_data == expected


def test_should_return_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    assert restore_names(users) is None
