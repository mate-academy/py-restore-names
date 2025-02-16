import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,exp_first_name",
    [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }], "Jack"),
        ([{
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }], "Jack")
    ]
)
def test_first_name_is_restored(
        users: list[dict],
        exp_first_name: str
) -> None:
    restore_names(users)
    assert users[0]["first_name"] == exp_first_name
