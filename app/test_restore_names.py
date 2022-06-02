import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_incoming,user_output",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            "Jack",
            id="first name is None"
        ),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            "Mike",
            id="first name is not exist"
        )
    ]
)
def test_first_name_restored(user_incoming: list,
                             user_output: str):
    restore_names(user_incoming)
    assert user_incoming[0]["first_name"] == user_output
