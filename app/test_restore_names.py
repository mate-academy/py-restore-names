import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_data() -> list[dict]:
    return [
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


def test_user_first_name_plus_surname_equal_to_full_name(
        users_data: list[dict]
) -> None:
    restore_names(users_data)
    for user in users_data:
        first_name = user.get("first_name")
        last_name = user.get("last_name")
        full_name = user.get("full_name")
        assert f"{first_name} {last_name}" == full_name
