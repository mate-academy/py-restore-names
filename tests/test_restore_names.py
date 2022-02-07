from app.restore_names import restore_names
import pytest


@pytest.mark.parametrize(
    "users,expected",
    [
        pytest.param(
                    [
                        {
                            "first_name": "Mike",
                            "last_name": "Adams",
                            "full_name": "Mike Adams",
                        },
                        {
                            "first_name": "Anita",
                            "last_name": "Posledova",
                            "full_name": "Anita Posledova",
                        },
                    ],
                    [
                        {
                            "first_name": "Mike",
                            "last_name": "Adams",
                            "full_name": "Mike Adams",
                        },
                        {
                            "first_name": "Anita",
                            "last_name": "Posledova",
                            "full_name": "Anita Posledova",
                        },
                    ],
                    id="should return the same list, when all keys `first_name` have strings as values"
        ),
        pytest.param(
                    [
                        {
                            "first_name": None,
                            "last_name": "Adams",
                            "full_name": "Mike Adams",
                        },
                        {
                            "first_name": None,
                            "last_name": "Posledova",
                            "full_name": "Anita Posledova",
                        },
                    ],
                    [
                        {
                            "first_name": "Mike",
                            "last_name": "Adams",
                            "full_name": "Mike Adams",
                        },
                        {
                            "first_name": "Anita",
                            "last_name": "Posledova",
                            "full_name": "Anita Posledova",
                        },
                    ],
                    id="should return filled-in list, when the key `first_name` has None as value"
        ),
        pytest.param(
                    [
                        {
                            "last_name": "Adams",
                            "full_name": "Mike Adams",
                        },
                        {
                            "last_name": "Posledova",
                            "full_name": "Anita Posledova",
                        },
                    ],
                    [
                        {
                            "first_name": "Mike",
                            "last_name": "Adams",
                            "full_name": "Mike Adams",
                        },
                        {
                            "first_name": "Anita",
                            "last_name": "Posledova",
                            "full_name": "Anita Posledova",
                        },
                    ],
                    id="should return filled-in list, when there are no keys `first_name`"
        ),
    ]
)
def test_is_result_correct(users, expected):
    restore_names(users)
    assert users == expected
