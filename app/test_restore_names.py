import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,restored", [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }], [{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }]), ([{
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }], [{
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }]),
        ([{
            "last_name": "Gamma",
            "full_name": "Narberal Gamma",
        }], [{
            "first_name": "Narberal",
            "last_name": "Gamma",
            "full_name": "Narberal Gamma",
        }]), ([{
            "first_name": None,
            "last_name": "Douson",
            "full_name": "Jack Douson",
        }], [{
            "first_name": "Jack",
            "last_name": "Douson",
            "full_name": "Jack Douson",
        }])
    ]
)
def test_restore_names_should_restore_correctly(
    users: list,
    restored: list
) -> None:
    restore_names(users)
    assert users == restored
