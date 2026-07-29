import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_list,list_with_restored_names",
    [
        (
            [
                {
                    "first_name": "Kyle",
                    "last_name": "MacLachlan",
                    "full_name": "Kyle MacLachlan",
                }
            ],
            [
                {
                    "first_name": "Kyle",
                    "last_name": "MacLachlan",
                    "full_name": "Kyle MacLachlan",
                }
            ]
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Fenn",
                    "full_name": "Sherilyn Fenn",
                }
            ],
            [
                {
                    "first_name": "Sherilyn",
                    "last_name": "Fenn",
                    "full_name": "Sherilyn Fenn",
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Lee",
                    "full_name": "Sheryl Lee",
                },
                {
                    "last_name": "Ashbrook",
                    "full_name": "Dana Ashbrook",
                }
            ],
            [
                {
                    "first_name": "Sheryl",
                    "last_name": "Lee",
                    "full_name": "Sheryl Lee",
                },
                {
                    "first_name": "Dana",
                    "last_name": "Ashbrook",
                    "full_name": "Dana Ashbrook",
                }
            ]
        )
    ],
    ids=[
        "should not change anything if first names are correct",
        "should change None to valid name",
        "should add 'first_name' field and add valid name"
    ]

)
def test_first_name_is_restored(
        users_list: list[dict],
        list_with_restored_names: list[dict]
) -> None:
    restore_names(users_list)
    assert users_list == list_with_restored_names
