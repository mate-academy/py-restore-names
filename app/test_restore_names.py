import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list:
    return [
        {"first_name": "Jack",
         "full_name": "Jack Holy",
         "last_name": "Holy"
         }]


@pytest.mark.parametrize("users",
                         [
                             ([{
                                 "first_name": None,
                                 "last_name": "Holy",
                                 "full_name": "Jack Holy",
                             }]),
                             ([{
                                 "last_name": "Holy",
                                 "full_name": "Jack Holy",
                             }]),
                             ([{
                                 "first_name": "Jack",
                                 "last_name": "Holy",
                                 "full_name": "Jack Holy",
                             }])
                         ],
                         ids=[
                             "first name None",
                             "no first name",
                             "all data correct"
                         ])
def test_restore_names(user_template: list, users: list[dict]) -> None:
    restore_names(users)
    assert users == user_template
