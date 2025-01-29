import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,result",
    [
        ([{"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}],
         ["Jack"]),
        ([{"last_name": "Adams", "full_name": "Mike Adams"}], ["Mike"]),
        ([{"first_name": "Mike", "last_name": "Adams",
           "full_name": "Mike Adams"}], ["Mike"]),
        ([{"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"
           }], ["Jack"]),
        ([{"full_name": "Barack Obama"},
          {"full_name": "Donald Trump"},
          {"first_name": None, "full_name": "George R.R. Martin"},
          {"first_name": "Ada", "full_name": "Ada Lovelace"}],
         ["Barack", "Donald", "George", "Ada"])
    ],
    ids=[
        "first name none",
        "first name missing",
        "first name already present",
        "first name already present",
        "multiple users"
    ]
)
def test_restore_names(users: list, result: set) -> None:
    restore_names(users)
    for idx in range(len(users)):
        assert users[idx]["first_name"] == result[idx]
