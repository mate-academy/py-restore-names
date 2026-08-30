import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, result",
    [
        pytest.param(
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
            id="check-one-user-with-existing-first_name",
        ),
        pytest.param(
            [
                {
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
            id="check-one-user-without-first_name",
        ),
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Black",
                    "full_name": "Jack Black",
                },
                {
                    "first_name": None,
                    "last_name": "Smith",
                    "full_name": "Bob Smith",
                },
                {
                    "last_name": "Gwen",
                    "full_name": "Stacy Gwen",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Jack",
                    "last_name": "Black",
                    "full_name": "Jack Black",
                },
                {
                    "first_name": "Bob",
                    "last_name": "Smith",
                    "full_name": "Bob Smith",
                },
                {
                    "first_name": "Stacy",
                    "last_name": "Gwen",
                    "full_name": "Stacy Gwen",
                },
            ],
            id="check-multiple-users",
        ),
    ],
)
def test_restore_names(users: list, result: list) -> None:
    restore_names(users)
    assert users == result
