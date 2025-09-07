import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,result",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            "Jack"
        ),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            "Mike"
        ),
        (
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            "Jack"
        ),
        (
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            "Mike"
        )
    ]
)
def test_logic_restore_names(users: list, result: str) -> None:
    restore_names(users)
    assert users[0]["first_name"] == result


def test_without_complete_name() -> None:
    user = [
        {
            "first_name": None,
            "last_name": "Adams",
        }
    ]
    with pytest.raises(KeyError):
        restore_names(user)
