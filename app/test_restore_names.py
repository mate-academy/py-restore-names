import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_of_users,expected",
    [
        pytest.param([
            {"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"}
        ],
            [
            {"first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"}
        ],
            id="should use first name from the string 'full name'"
        ),
        pytest.param([
            {"last_name": "Holy",
             "full_name": "Jack Holy"},
            {"first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"}
        ],
            [
            {"first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"}
        ],
            id="should add 'first name' key with correct name"
        )
    ]
)
def test_restore_names_function(
        list_of_users: list[dict],
        expected: list[dict]
) -> None:
    restore_names(list_of_users)
    assert list_of_users == expected
