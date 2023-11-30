import pytest
from app.restore_names import restore_names


@pytest.fixture()
def user_fixture() -> list[dict[str, str | None] | dict[str, str]]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


def test_restore_names(user_fixture: list) -> None:
    restore_names(user_fixture)
    assert user_fixture[0]["first_name"] == "Jack"
    assert user_fixture[1]["first_name"] == "Mike"
