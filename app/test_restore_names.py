import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        ([{"first_name": None,
           "last_name": "Jordan",
           "full_name": "Michael Jordan"}],
         [{"first_name": "Michael",
           "last_name": "Jordan",
           "full_name": "Michael Jordan"}]),
        ([{"first_name": "Dennis",
           "last_name": "Rodman",
           "full_name": "Dennis Rodman"}],
         [{"first_name": "Dennis",
           "last_name": "Rodman",
           "full_name": "Dennis Rodman"}]),
        ([{"last_name": "Pippen",
           "full_name": "Scottie Pippen"}],
         [{"first_name": "Scottie",
           "last_name": "Pippen",
           "full_name": "Scottie Pippen"}])
    ]
)
def test_restore_names(users: list[dict],
                       expected: dict) -> None:
    restore_names(users)
    assert users == expected
