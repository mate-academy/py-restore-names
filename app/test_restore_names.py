import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected_name",
    [
        ([{
            "first_name": None,
            "last_name": "Blackbeak",
            "full_name": "Elathrin Blackbeak"
        }], "Elathrin"),
        ([{
            "last_name": "Blackbeak",
            "full_name": "Elathrin Blackbeak"
        }], "Elathrin"),

    ]
)
def test_should_restore_first_name(
        users: list[dict],
        expected_name: str
) -> None:
    restore_names(users)
    assert users[0]["first_name"] == expected_name
