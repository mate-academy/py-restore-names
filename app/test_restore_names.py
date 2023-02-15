import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_dict_template() -> list[dict]:
    return [
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


def test_normal(user_dict_template: list[dict]) -> None:
    restore_names(user_dict_template)
    assert user_dict_template == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"},
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
            "first_name": "Mike"}
    ]
