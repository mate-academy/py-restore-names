import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_input, users_result",
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
            id="test when first_name is None"
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
            id="test when key 'first_name' doesn't exist"
        ),
        pytest.param(
            [
                {
                    "first_name": "Jack",
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
            id="test when first_name is filled"
        )
    ]
)
def test_restore_names(
        users_input: list[dict],
        users_result: list[dict]
) -> None:
    restore_names(users_input)
    assert (
        users_input == users_result
    )
