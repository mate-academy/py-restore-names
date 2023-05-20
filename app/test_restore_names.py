import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_name():
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }]


def test_should_set_correct_name(user_name) -> None:
    names_to_restore = [
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
    restore_names(names_to_restore)
    assert user_name == names_to_restore
