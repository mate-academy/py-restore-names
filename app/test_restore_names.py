import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        pytest.param(
            [{"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}],
            [{"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}],
            id="test_if_first_name_is_None"
        ),
        pytest.param(
            [{"last_name": "Adams", "full_name": "Mike Adams"}],
            [{"first_name": "Mike", "last_name": "Adams", "full_name": "Mike Adams"}],
            id="test_if_first_name_is_missing"
        ),
        pytest.param(
            [{"first_name": "Harry", "last_name": "Potter", "full_name": "Harry Potter"}],
            [{"first_name": "Harry", "last_name": "Potter", "full_name": "Harry Potter"}],
            id="test_if_all_info_is_valid"
        )
    ]
)
def test_(users: list[dict], expected: dict) -> None:
    restore_names(users)
    assert users == expected
