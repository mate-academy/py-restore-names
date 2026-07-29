import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.mark.parametrize(
    "users",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            id="Should restore name if name is 'None'",
        ),
        pytest.param(
            [
                {
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            id="Should restore name if user dict dont have 'first_name' key",
        ),
    ],
)
def test_should_restore_names_correctly(
    users: list, users_template: callable
) -> None:
    restore_names(users)
    assert users == users_template
