import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_user, expected_first_name",
    [
        (
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            "Jack"
        ),
        (
            {
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
            "Mike"
        ),
        (
            {
                "first_name": "Existing",
                "full_name": "Don't Change Me"
            },
            "Existing"
        ),
    ],
)
def test_restore_names_parametrized(
        initial_user: dict,
        expected_first_name: str
) -> None:
    users = [initial_user]

    restore_names(users)

    assert users[0]["first_name"] == expected_first_name
