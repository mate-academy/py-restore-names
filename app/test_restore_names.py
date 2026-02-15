import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_origin, correct_dict_of_users",
    [
        ([{"first_name": "John", "last_name": "Smith",
           "full_name": "John Smith"}],
         [{"first_name": "John", "last_name": "Smith",
           "full_name": "John Smith"}]),
        ([{"last_name": "Kovbasa", "full_name": "Petro Kovbasa"}],
         [{"first_name": "Petro", "last_name": "Kovbasa",
           "full_name": "Petro Kovbasa"}]),
        ([{"first_name": None, "last_name": "Holy",
           "full_name": "Jack Holy"}],
         [{"first_name": "Jack", "last_name": "Holy",
           "full_name": "Jack Holy"}])
    ],
    ids=[
        "Test modified dictionary if first name contains correct value",
        "Test modified dictionary if first name item does not exist",
        "Test modified dictionary first name value contains None"
    ]
)
def test_first_name_value_correction(
        users_origin: list,
        correct_dict_of_users: list
) -> None:
    restore_names(users_origin)
    assert users_origin == correct_dict_of_users, \
        (f"Modified dictionary of users should be equal to: "
         f"{correct_dict_of_users}")
