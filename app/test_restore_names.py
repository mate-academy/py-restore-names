import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list,expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ], "Jack"),
        (
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ], "Mike"),
        (
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ], "Jack"),
        (
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ], "Mike")
    ]
)
def test_restore_names(users_list: list[dict], expected: str) -> None:
    restore_names(users_list)
    assert users_list[0]["first_name"] == expected
