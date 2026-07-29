import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,result",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            id="User with `first_name` = None"
        ),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ],
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                    "first_name": "Mike"
                }
            ],
            id="User without `first_name`"
        ),
        pytest.param(
            [
                {
                    "first_name": "James",
                    "last_name": "Smith",
                    "full_name": "James Smith"
                }
            ],
            [
                {
                    "first_name": "James",
                    "last_name": "Smith",
                    "full_name": "James Smith"
                }
            ],
            id="User with correct first name"
        ),
        pytest.param(
            [
                {
                    "first_name": "Julia",
                    "last_name": "Sirko",
                    "full_name": "Sviatoslava Sirko"
                }
            ],
            [
                {
                    "first_name": "Julia",
                    "last_name": "Sirko",
                    "full_name": "Sviatoslava Sirko"
                }
            ],
            id="User with incorrect first name"
        )
    ]
)
def test_different_values_of_first_name(users: list, result: list) -> None:
    restore_names(users)
    assert (
        users == result
    ), f"{users} should be equal to {result}"
