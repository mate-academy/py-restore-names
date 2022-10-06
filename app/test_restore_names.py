import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list,expected_result",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ], "Jack",
            id="first name is 'None'"
        ),
        pytest.param(
            [
                {
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ], "Jack",
            id="dict not have key 'first_name'"
        ),
    ]
)
def test_correct_first_name(users_list: list, expected_result: str):
    restore_names(users_list)
    for user in users_list:
        assert user["first_name"] == expected_result
