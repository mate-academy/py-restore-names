import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        (
            # input
            [{"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}],
            # output esperado
            [{"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}],
        ),
        (
            # input
            [{"first_name": "", "last_name": "Holy", "full_name": "Jack Holy"}],
            # output esperado
            [{"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}],
        ),
        (
            # input
            [{"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}],
            # output esperado
            [{"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}],
        ),
    ],
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected
