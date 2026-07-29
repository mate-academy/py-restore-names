import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_input_first_set() -> list[dict]:
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
        {
            "first_name": None,
            "last_name": "Zabolotnyi",
            "full_name": "Vlad Zabolotnyi",
        }
    ]


@pytest.fixture()
def users_input_second_set() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Red",
            "full_name": "Kate Red",
        },
        {
            "last_name": "lloyd",
            "full_name": "bob lloyd",
        }
    ]


def test_restore_names_main_case(
        users_input_first_set: list,
        users_input_second_set: list
) -> None:
    restore_names(users_input_first_set)
    restore_names(users_input_second_set)
    assert users_input_first_set == [
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
        {
            "first_name": "Vlad",
            "last_name": "Zabolotnyi",
            "full_name": "Vlad Zabolotnyi",
        }
    ]
    assert users_input_second_set == [
        {
            "first_name": "Kate",
            "last_name": "Red",
            "full_name": "Kate Red",
        },
        {
            "first_name": "bob",
            "last_name": "lloyd",
            "full_name": "bob lloyd",
        }
    ]
