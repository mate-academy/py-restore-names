import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users",
    [
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ],
        [
            {
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ],
        [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ],
    ],
)
def test_restore_names_func(users: list) -> None:
    restore_names(users)
    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
