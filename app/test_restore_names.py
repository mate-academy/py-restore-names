import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        ([{"first_name": None,
           "last_name": "Sparrow",
           "full_name": "Jack Sparrow"}], "Jack"),
        ([{"last_name": "Man",
           "full_name": "Iron Man"}], "Iron")
    ]
)
def test_all_data_restore(
        users: list[dict],
        expected: str
) -> str:
    restore_names(users)
    assert users[0]["first_name"] == expected
