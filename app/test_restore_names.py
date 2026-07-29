import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            # first_name is None
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
        ),
        (
            # first_name is missing
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
        ),
        (
            # first_name is already present
            [
                {
                    "first_name": "Emily",
                    "last_name": "Stone",
                    "full_name": "Emily Stone",
                }
            ],
            [
                {
                    "first_name": "Emily",
                    "last_name": "Stone",
                    "full_name": "Emily Stone",
                }
            ],
        ),
        (
            # multiple users mixed
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
                    "first_name": "Emily",
                    "last_name": "Stone",
                    "full_name": "Emily Stone",
                },
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
                    "first_name": "Emily",
                    "last_name": "Stone",
                    "full_name": "Emily Stone",
                },
            ],
        ),
    ],
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    """
    Test restore_names by checking updated users list in-place.
    """
    restore_names(users)
    assert users == expected
