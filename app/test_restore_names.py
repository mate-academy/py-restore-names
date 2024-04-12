import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_of_users,result",
    [
        pytest.param([
            {"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"},
        ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike",
                 "last_name": "Adams",
                 "full_name": "Mike Adams"},
        ],
            id="test should add expected value for 'first_name'"
        ),
        pytest.param([
            {"first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"last_name": "Adams",
             "full_name": "Mike Adams"},
        ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy"},
                {"first_name": "Mike",
                 "last_name": "Adams",
                 "full_name": "Mike Adams"},
        ],
            id="test should add the key 'first_name'"
        )
    ]
)
def test_restore_names_function(
        list_of_users: list[dict],
        result: list[dict]) -> None:
    restore_names(list_of_users)
    assert list_of_users == result
