import pytest
from typing import List
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_result",
    [
        (
            [
                {"first_name": None, "last_name": "Hoffsteder",
                 "full_name": "Leonard Hoffsteder"},
                {"last_name": "Volovits", "full_name": "Govard Volovits"}
            ],
            ["Leonard", "Govard"]
        ),
        (
            [
                {"first_name": "Penny", "last_name": "Blossom",
                 "full_name": "Penny Blossom"},
                {"last_name": "Cutrapalli", "full_name": "Raj Cutrapalli"}
            ],
            ["Penny", "Raj"]
        )
    ]
)
def test_restore_names(users: List[dict], expected_result: List[str]) -> None:
    restore_names(users)
    for user, expected_name in zip(users, expected_result):
        assert user["first_name"] == expected_name
