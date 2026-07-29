import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_pattern() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Black",
            "full_name": "Holy Black",
        },
        {
            "last_name": "Bardugo",
            "full_name": "Lee Bardugo",
        },
    ]


def test_func_should_restore_names(user_pattern: list[dict]) -> None:
    restore_names(user_pattern)
    assert user_pattern[0]["first_name"] == "Holy"
    assert user_pattern[1]["first_name"] == "Lee"
