import pytest
from app.restore_names import restore_names


@pytest.fixture
def users_templates() -> list:
    yield [
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


def test_should_return_dict_with_first_name(users_templates: list) -> None:
    restore_names(users_templates)
    assert users_templates == [
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
