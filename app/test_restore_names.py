import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list, expected",
    [
        ([{"first_name": "John", "full_name": "John Doe"}], "John"),
        ([{"full_name": "John Doe"}], "John"),
        ([{"first_name": None, "full_name": "John Doe"}], "John"),
    ]
)
def test_restore_names(users_list: list, expected: str) -> None:
    restore_names(users_list)
    assert users_list[0]["first_name"] == expected
