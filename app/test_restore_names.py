import pytest


from app.restore_names import restore_names


@pytest.fixture()
def users_init() -> list[dict]:
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


@pytest.fixture()
def users_restored() -> list[dict]:
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
        },
    ]


def test_restore_names_when_name_none(
    users_init: list[dict], users_restored: list[dict]
) -> None:
    restore_names([users_init[0]])
    assert [users_init[0]] == [users_restored[0]]


def test_restore_names_when_name_does_not_exist(
    users_init: list[dict], users_restored: list[dict]
) -> None:
    restore_names([users_init[1]])
    assert [users_init[1]] == [users_restored[1]]


def test_restore_names_when_name_when_multiple_dict(
    users_init: list[dict], users_restored: list[dict]
) -> None:
    restore_names(users_init)
    assert users_init == users_restored


def test_restore_names_should_not_do_anything(
    users_init: list[dict], users_restored: list[dict]
) -> None:
    users_init[0]["first_name"] = "Jack"
    users_init[1]["first_name"] = "Mike"
    restore_names(users_init)
    assert users_init == users_restored
