import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,result",
    [
        ([
            {
                "first_name": None,
                "last_name": "Smith",
                "full_name": "John Smith"
            },
            {
                "last_name": "Black",
                "full_name": "Dave Smith"
            }],
            [
            {
                "first_name": "John",
                "last_name": "Smith",
                "full_name": "John Smith"
            },
            {
                "first_name": "Dave",
                "last_name": "Black",
                "full_name": "Dave Smith"
            }
        ]),
        ([
            {
                "first_name": None,
                "last_name": "Smith",
                "full_name": "Jane Smith"
            },
            {
                "last_name": "Dow",
                "full_name": "Bill Dow"
            }],
            [
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "full_name": "Jane Smith"
            },
            {
                "first_name": "Bill",
                "last_name": "Dow",
                "full_name": "Bill Dow"
            }
        ]),
    ]
)
def test_restore_names(users: list[dict], result: list[dict]) -> None:
    restore_names(users)
    assert users == result
