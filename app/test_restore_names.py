import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected",
    [
        (
            {
                "first_name": None,
                "full_name": "Jack Holy"
            },
            "Jack"
        ),
        (
            {
                "full_name": "Mike Adams"
            },
            "Mike"
        )
    ]
)
def test_restore_names(user: dict, expected: str) -> None:
    restore_names([user])
    assert user["first_name"] == expected
