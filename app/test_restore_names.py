import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_template() -> list[dict]:
    return [{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy", }]


@pytest.mark.parametrize("users", [
    ([{
      "first_name": None,
      "last_name": "Holy",
      "full_name": "Jack Holy", }]),
    ([{
      "last_name": "Holy",
      "full_name": "Jack Holy", }])
])
def test_restore_names(user_template: list[dict], users: list[dict]) -> None:
    restore_names(users)
    assert users == user_template
