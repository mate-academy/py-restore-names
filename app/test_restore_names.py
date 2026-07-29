import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_info() -> list:
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


def test_function_does_not_return_anything(
    users_info: list
) -> None:
    assert (
        restore_names(users_info) is None
    ), "Functions doesn't return anything"


def test_names_are_correctly_restored(
    users_info: list
) -> None:
    restore_names(users_info)

    for user in users_info:
        assert (
            user["first_name"] == user["full_name"].split()[0]
        ), "Names should be restored correctly"
