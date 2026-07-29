import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_input,user_output",
    [
        pytest.param(
            [
                {"first_name": None,
                 "last_name": "Holy",
                 "full_name": "Jack Holy"}
            ],
            "Jack",
            id="first name is None"
        ),
        pytest.param(
            [
                {"last_name": "Adams",
                 "full_name": "Mike Adams"}
            ],
            "Mike",
            id="no 'first name' in user"
        )
    ]
)
def test_restore_names(user_input: list,
                       user_output: str):
    restore_names(user_input)
    assert user_input[0]["first_name"] == user_output
