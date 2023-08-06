import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_name() -> list[dict[str, str] | dict[str, str]]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_should_set_correct_first_name(
        user_name: list[dict[str, str] | dict[str, str]]
) -> None:
    correct_name: list[dict[str, str] | None] = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(correct_name)
    assert user_name == correct_name
