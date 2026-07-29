import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Hrechko",
                    "full_name": "Andrii Hrechko",
                }
            ],
            [
                {
                    "first_name": "Andrii",
                    "last_name": "Hrechko",
                    "full_name": "Andrii Hrechko",
                }
            ],
        ),
        (
            [
                {
                    "last_name": "Hrechko",
                    "full_name": "Andrii Hrechko",
                }
            ],
            [
                {
                    "first_name": "Andrii",
                    "last_name": "Hrechko",
                    "full_name": "Andrii Hrechko",
                }
            ],
        ),
        ([], []),
    ],
    ids=["key name is none", "key name not exists", "empty list"],
)
def test_restore_names(
    users: list[dict[str, str]], expected: list[dict[str, str]]
) -> None:
    restore_names(users)
    assert users == expected
