import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users",
    [
        [{"first_name": None, "last_name": "Adams",
          "full_name": "Mike Adams"}],
        [{"last_name": "Holy", "full_name": "Jack Holy"}],
    ],
    ids=[
        "test restoration names when no last_name",
        "test restoration names when last_name equal None",
    ]
)
def test_restoration_names(users: list[dict]) -> None:
    restore_names(users)
    for user in users:
        assert user["full_name"].split()[0] == user.get("first_name")
