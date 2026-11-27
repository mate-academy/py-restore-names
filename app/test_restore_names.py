import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_result",
    [
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
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
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
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                },
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                },
            ],
        ),
        (
            [],
            [],
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
                    "first_name": "Bob",
                    "last_name": "Brown",
                    "full_name": "Robert Brown",
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
                    "first_name": "Bob",
                    "last_name": "Brown",
                    "full_name": "Robert Brown",
                },
            ],
        ),
    ]
)
def test_restore_names(users: dict, expected_result: dict) -> None:
    restore_names(users)
    assert users == expected_result


@pytest.mark.parametrize(
    "users",
    [
        1,
        1.01,
        "1"
    ]
)
def test_wrong_type(users: int | float | str | list) -> None:
    with pytest.raises(TypeError):
        restore_names(users)
