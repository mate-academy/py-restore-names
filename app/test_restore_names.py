import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        ([{"first_name": None,
           "last_name": "Holy",
           "full_name": "Jack Holy"}], "Jack"),
        ([{"last_name": "Holy",
            "full_name": "Jack Holy"}], "Jack"),
        ([{"first_name": "Alice",
            "last_name": "Holy",
            "full_name": "Alice Holy"}], "Alice"),
    ]
)
def test_restore_names(users: dict, expected: str) -> None:
    restore_names(users)
    assert users[0]["first_name"] == expected
