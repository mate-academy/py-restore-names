import pytest
from app.restore_names import restore_names


@pytest.fixture()
def fixed_user_data() -> list[dict]:
    return [
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
    ]


@pytest.mark.parametrize(
    "users",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": None,
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            id="Function should restore name when `first name` is `None`"
        ),
        pytest.param(
            [
                {
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            id="Function should restore name when `first name` key is missing"
        )
    ]
)
def test_restore_name(users: list[dict], fixed_user_data: list[dict]) -> None:
    restore_names(users)
    assert users == fixed_user_data
