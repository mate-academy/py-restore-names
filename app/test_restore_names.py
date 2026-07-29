import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,result",
    [
        ([{"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}],
         ["Jack"]),
        ([{"last_name": "Adams", "full_name": "Mike Adams"}], ["Mike"]),
        ([{"first_name": "Jack", "last_name": "Holy",
           "full_name": "Jack Holy"}], ["Jack"]),
        ([{"full_name": "Mark Twain"},
          {"first_name": None, "full_name": "Samuel Clemens"},
          {"first_name": "Leo", "full_name": "Leo Tolstoy"}],
         ["Mark", "Samuel", "Leo"])
    ],
    ids=[
        "first name none",
        "first name missing",
        "first name already present",
        "multiple users"
    ]
)
def test_restore_names(users: list, result: str) -> None:
    restore_names(users)
    for i in range(len(users)):
        assert users[i]["first_name"] == result[i]
