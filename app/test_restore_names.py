import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_result",
    [
        ({"first_name": None,
          "last name": "Wayne",
          "full_name": "Bruce Wayne"},

         {"first_name": "Bruce",
          "last name": "Wayne",
          "full_name": "Bruce Wayne"}),

        ({"last_name": "Adams",
          "full_name": "Mike Adams"},

         {"first_name": "Mike",
          "last_name": "Adams",
          "full_name": "Mike Adams"})
    ]
)
def test_restore_names(users: dict, expected_result: dict) -> None:
    restore_names([users])
    assert users == expected_result
