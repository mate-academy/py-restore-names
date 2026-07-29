import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_of_users, result",
    [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }], [{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }]),
        ([{
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }], [{
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }])
    ]
)
def test_restoring_names(
        list_of_users: list[dict],
        result: list[dict]
) -> None:
    restoring = list_of_users
    restore_names(restoring)
    assert restoring == result
