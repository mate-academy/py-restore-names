import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, restored_names",
    [
        ([{"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
          {"last_name": "Adams", "full_name": "Mike Adams"}],
         ["Jack", "Mike"])
    ]
)
def test_restore_names(users: list, restored_names: list) -> None:
    restore_names(users)
    first_names = []
    for user in users:
        first_names.append(user["first_name"])
    assert first_names == restored_names
