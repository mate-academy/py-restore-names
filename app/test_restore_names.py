import copy
import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user,expected_first_name", [
        ([{"first_name": None, "full_name": "Mike Adams"}], "Mike"),
        ([{"full_name": "Jack Holy"}], "Jack")
    ]
)
def test_restore_name(user: list, expected_first_name: str) -> None:
    restore_names(user)
    assert user[0]["first_name"] == expected_first_name


def test_restore_names_does_nothing_if_first_name_present() -> None:
    user = [{
        "first_name": "Alice",
        "last_name": "Johnson",
        "full_name": "Alice Johnson"
    }]
    original = copy.deepcopy(user)

    restore_names(user)

    assert user == original
