import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_result",
    [
        ({"first_name": None,
          "last name": "Wayne",
          "full_name": "Lil Wayne"},

         {"first_name": "Lil",
          "last name": "Wayne",
          "full_name": "Lil Wayne"}),

        ({"last_name": "Smith",
          "full_name": "Mr Smith"},

         {"first_name": "Mr",
          "last_name": "Smith",
          "full_name": "Mr Smith"})
    ]
)
def test_restore_names(users: dict, expected_result: dict) -> None:
    restore_names([users])
    assert users == expected_result
