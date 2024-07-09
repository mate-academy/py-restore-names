import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, first_names", [
        ([
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ], ["Jack"]),
        ([
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ], ["Mike"]),
        ([
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ], ["Jack", "Mike"]),
    ]
)
def test_restore_names(users: list, first_names: list) -> None:
    restore_names(users)
    for index, user in enumerate(users):
        assert user["first_name"] == first_names[index]
