import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_result",
    [
        (
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },
                {
                    "last_name": "Smith",
                    "full_name": "John Smith"
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith"
                },
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith"
                }
            ]
        )
    ]
)
def test_restore_names(
        users: list[dict],
        expected_result: dict
) -> None:
    restore_names(users)
    assert users == expected_result
