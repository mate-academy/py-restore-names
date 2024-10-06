import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    ("users", "expected"),
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ]
        ),
        (
            [
                {
                    "full_name": "Elisabet Williams",
                },
            ],
            [
                {
                    "first_name": "Elisabet",
                    "full_name": "Elisabet Williams",
                }
            ]
        ),
    ]
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected
