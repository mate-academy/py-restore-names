import pytest
from app.restore_names import restore_names

@pytest.mark.parametrize(
    "users, expected_names",
    [
        (
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    },
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                    {
                        "first_name": "John",
                        "last_name": "Doe",
                        "full_name": "Fake Name",
                    }
                ],
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    },
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                    {
                        "first_name": "John",
                        "last_name": "Doe",
                        "full_name": "Fake Name",
                    }

                ]
        )
    ]
)
def test_restore_names(users, expected_names):
    restore_names(users)
    assert users == expected_names
