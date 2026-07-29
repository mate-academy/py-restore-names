import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_users, expected_users",
    [
        (
            [
                {"last_name": "Adams", "full_name": "Mike Adams"},
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
        ),
        (
            [
                {
                    "first_name": "",
                    "last_name": "Smith",
                    "full_name": "Will Smith",
                },
            ],
            [
                {
                    "first_name": "",
                    "last_name": "Smith",
                    "full_name": "Will Smith",
                },
            ],
        ),
        (
            [
                {
                    "first_name": "Anna",
                    "last_name": "Bell",
                    "full_name": "Anna Bell",
                },
            ],
            [
                {
                    "first_name": "Anna",
                    "last_name": "Bell",
                    "full_name": "Anna Bell",
                },
            ],
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
                {
                    "first_name": "Sara",
                    "last_name": "Connor",
                    "full_name": "Sara Connor",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
                {
                    "first_name": "Sara",
                    "last_name": "Connor",
                    "full_name": "Sara Connor",
                },
            ],
        ),
    ],
    ids=[
        "missing_first_name",
        "first_name_none",
        "first_name_empty_str",
        "first_name_present",
        "mixed_users",
    ],
)
def test_restore_names(
    input_users: List[dict], expected_users: List[dict]
) -> None:
    result = restore_names(input_users)
    assert result is None
    assert input_users == expected_users
