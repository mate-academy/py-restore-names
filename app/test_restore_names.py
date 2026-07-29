import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "one_users, two_users",
    [
        pytest.param(
            [
                {"first_name": None, "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"last_name": "Adams", "full_name": "Mike Adams"},
            ],
            [
                {"first_name": "Jack", "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike", "last_name": "Adams",
                 "full_name": "Mike Adams"},
            ],
            id="one test"),
        pytest.param(
            [
                {"first_name": None, "last_name": "Shulika",
                 "full_name": "Liza Shulika"},
                {"last_name": "Adar", "full_name": "Lina Adar"},
            ],
            [
                {"first_name": "Liza", "last_name": "Shulika",
                 "full_name": "Liza Shulika"},
                {"first_name": "Lina", "last_name": "Adar",
                 "full_name": "Lina Adar"},
            ],
            id="two test"),
    ]
)
def test_restore_names(one_users: list[dict], two_users: list[dict]) -> None:
    restore_names(one_users)
    assert one_users == two_users
