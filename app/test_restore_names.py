import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list[dict]:
    return [
        {
            "first_name": "Vladyslav",
            "last_name": "Prokopiv",
            "full_name": "Vladyslav Prokopiv"
        }
    ]


def test_check_if_first_name_is_none(users_template: list[dict]) -> None:
    users_template[0]["first_name"] = None
    restore_names(users_template)
    expected = users_template[0]["full_name"].split()[0]

    assert users_template[0]["first_name"] == expected, \
        "'first_name' shold be equal 'Vladyslav'"


def test_check_if_first_name_not_in_dict(users_template: list[dict]) -> None:
    del users_template[0]["first_name"]
    restore_names(users_template)
    expected = users_template[0]["full_name"].split()[0]

    assert users_template[0]["first_name"] == expected, \
        "'first_name' shold be equal 'Vladyslav'"
