import pytest
from app.restore_names import restore_names


# write your tests here
@pytest.mark.parametrize(
    "users,result",
    [
        ([{"last_name": "Holy",
           "full_name": "Jack Holy"},
          {"first_name": "Mike",
           "last_name": "Adams",
           "full_name": "Mike Adams"}],
         [{"first_name": "Jack",
           "last_name": "Holy",
           "full_name": "Jack Holy"},
          {"first_name": "Mike",
           "last_name": "Adams",
           "full_name": "Mike Adams"}]),
        ([{"first_name": "Jack",
           "last_name": "Holy",
           "full_name": "Jack Holy"},
          {"first_name": None,
           "last_name": "Adams",
           "full_name": "Mike Adams"}],
         [{"first_name": "Jack",
           "last_name": "Holy",
           "full_name": "Jack Holy"},
          {"first_name": "Mike",
           "last_name": "Adams",
           "full_name": "Mike Adams"}]),
    ]
)
def test_user_name_fixa(
    users: list[dict],
    result: list[dict]
) -> None:
    restore_names(users)
    assert (
        users == result
    ), ("Users first names have not been correctly set")
