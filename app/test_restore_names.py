import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_user,expected_user",
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
            id="User should have first name not None"
        ),
        pytest.param(
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
            id="Should add first name"
        ),
    ]
)
def test_user_should_have_first_name(
        initial_user,
        expected_user
):
    restore_names(initial_user)
    assert initial_user == expected_user
