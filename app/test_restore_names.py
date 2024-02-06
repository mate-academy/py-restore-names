import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_list, expected_result",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Black",
                    "full_name": "John Black"
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Black",
                    "full_name": "John Black"
                }
            ]
        ),
        (
            [
                {
                    "last_name": "Seinfeld",
                    "full_name": "Jerry Seinfeld"
                },
                {
                    "last_name": "Seinfeld",
                    "full_name": "Jerry Seinfeld"
                }
            ],
            [
                {
                    "first_name": "Jerry",
                    "last_name": "Seinfeld",
                    "full_name": "Jerry Seinfeld"
                },
                {
                    "first_name": "Jerry",
                    "last_name": "Seinfeld",
                    "full_name": "Jerry Seinfeld"
                }

            ]
        )
    ]
)
def test_when_first_name_is_none(user_list: list[dict],
                                 expected_result: list[dict]) -> None:
    restore_names(user_list)
    assert user_list == expected_result
