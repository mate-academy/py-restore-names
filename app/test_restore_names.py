import pytest
# from app.restore_names import restore_names


@pytest.fixture()
def list_of_users() -> list:
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


def test_when_first_name_is_none(list_of_users: list[dict]) -> None:

    restore_names_user = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    assert list_of_users[0].restore_names() == restore_names_user


def test_when_first_name_is_absent(list_of_users: list[dict]) -> None:

    restore_names_user = [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    assert list_of_users[1].restore_names() == restore_names_user
