import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list1, get_restore_names_res1",
    [(
        [{
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }],
        [{
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }]
    )]
)
def test_restore_only_missing_names(
        users_list1: list,
        get_restore_names_res1: list
) -> None:
    restore_names(users_list1)
    assert users_list1 == get_restore_names_res1


@pytest.mark.parametrize(
    "users_list2, get_restore_names_res2",
    [
        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }]
        )
    ]
)
def test_restore_only_none_names(
        users_list2: list,
        get_restore_names_res2: list
) -> None:
    restore_names(users_list2)
    assert users_list2 == get_restore_names_res2
