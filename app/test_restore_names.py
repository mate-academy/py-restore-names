import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:

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


def test_func_should_add_first_name_key_to_dict(users_template: list) -> None:
    restore_names(users_template)

    assert "first_name" in users_template[1]


def test_func_should_add_first_name_to_dict_with_none(
        users_template: list
) -> None:
    restore_names(users_template)

    assert users_template[0]["first_name"] == "Jack"
