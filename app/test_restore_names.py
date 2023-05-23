import pytest
from app.restore_names import restore_names

# write your tests here


@pytest.fixture()
def user_template() -> list:
    return [{"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"last_name": "Adams",
             "full_name": "Mike Adams"}]


def test_for_restore_names_first_name_user(user_template: list) -> None:
    restore_names(user_template)
    assert user_template == [{"first_name": "Jack",
                              "last_name": "Holy",
                              "full_name": "Jack Holy"},
                             {"first_name": "Mike",
                              "last_name": "Adams",
                              "full_name": "Mike Adams"}]
