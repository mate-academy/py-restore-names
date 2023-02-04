import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_template() -> list:
    return [
        {
            "first_name": None,
            "last_name": "Weber",
            "full_name": "Luke Weber",
        },
        {
            "last_name": "Pikula",
            "full_name": "Tina Pikula",
        },
    ]


def test_should_restore_first_name(users_template: list) -> None:
    restore_names(users_template)

    assert users_template[0]["first_name"] == "Luke"
    assert users_template[1]["first_name"] == "Tina"


def test_should_get_first_name_if_surname_is_same(
    users_template: list
) -> None:
    users_template[0]["last_name"] = "Luke"
    users_template[0]["full_name"] = "Luke Luke"

    users_template[1]["last_name"] = "Tina"
    users_template[1]["full_name"] = "Tina Tina"

    restore_names(users_template)

    assert users_template[0]["first_name"] == "Luke"
    assert users_template[1]["first_name"] == "Tina"


def test_should_get_first_name_with_no_last_name_given(
    users_template: list
) -> None:
    users_template[0].pop("last_name")
    users_template[1].pop("last_name")

    restore_names(users_template)

    assert users_template[0]["first_name"] == "Luke"
    assert users_template[1]["first_name"] == "Tina"


def test_should_not_change_first_name_if_its_given(
    users_template: list
) -> None:
    users_template[0]["first_name"] = "Luke_test"
    users_template[1]["first_name"] = "Tina_test"

    restore_names(users_template)

    assert users_template[0]["first_name"] == "Luke_test"
    assert users_template[1]["first_name"] == "Tina_test"
