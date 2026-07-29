import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users",
    [
        [
            {
                "first_name": "Jack",
                "last_name": "Holly",
                "full_name": "Jack Holly"
            },
            {
                "first_name": None,
                "last_name": "Holly",
                "full_name": "Jack Holly"
            },
            {
                "first_name": "",
                "last_name": "Holly",
                "full_name": "Jack Holly"
            },
            {
                "last_name": "Holly",
                "full_name": "Jack Holly"
            },

            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
            {
                "first_name": None,
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
            {
                "first_name": "",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
        ]
    ]


)
def test_restore_names(users: list[dict]) -> None:

    restore_names(users)
    for user in users:
        expected_first = user["full_name"].split()[0]
        assert user["first_name"] == expected_first
