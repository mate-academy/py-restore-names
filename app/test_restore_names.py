import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("user_data, expected_name", [
    ({"full_name": "Jack Holy"}, "Jack"),
    ({"first_name": None, "full_name": "Jack Holy"}, "Jack"),
    ({"first_name": "Mike", "full_name": "Alex Dodepovich"}, "Mike"),
    ({"full_name": "John Ronald Reuel"}, "John"),
])
def test_restore_names(user_data: dict, expected_name: str) -> None:
    users_list = [user_data]
    restore_names(users_list)
    assert users_list[0]["first_name"] == expected_name
