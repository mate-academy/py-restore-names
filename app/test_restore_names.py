import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_name",
    [
        ([
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ], "Jack"),

        ([
            {
                "last_name": "Adams",
                "full_name": "Mike Adams"
            }
        ], "Mike"),

    ]
)
def test_restore_names(
        users: list[dict],
        expected_name: str
) -> None:
    restore_names(users)
    func_result = users[0]
    assert func_result["first_name"] == expected_name
