import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list[dict]:
    return (
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
    )


def test_restore_name_if_user_do_not_have_first_name_or_none(
        user_template: list[dict]) -> None:
    restore_names(user_template)
    assert user_template == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
