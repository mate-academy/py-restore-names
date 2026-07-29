import pytest
from app import restore_names


@pytest.mark.parametrize(
    "input_user, expected_first",
    [
        ([{"first_name": None,
           "last_name": "Wick",
           "full_name": "John Wick"}],
         "John"),
        ([{"first_name": None,
           "last_name": "Einstein",
           "full_name": "Albert Einstein"}],
         "Albert"),
        ([{"last_name": "Smith",
           "full_name": "John Smith"}],
         "John"),
        ([{"first_name": "Adam",
           "last_name": "Smasher",
           "full_name": "Adam Smasher"}],
         "Adam"),
    ]
)
def test_restore_first_name(input_user: list[dict],
                            expected_first: str) -> None:
    users = [dict(u) for u in input_user]
    restore_names.restore_names(users)
    # assert "first_name" not in users[4]
    assert users[0].get("first_name") == expected_first
