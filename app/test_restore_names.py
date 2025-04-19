import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_input, users_output",
    [
        pytest.param([
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ], [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ]
        )
    ],
    ids=[
        "Should return correct first name when it's None",
        "Should return correct first name when it's absent"
    ]
)
def test_correct_first_name_restoration(
        users_input: list[dict],
        users_output: list[dict]
) -> None:
    restore_names(users_input)
    assert users_input == users_output
