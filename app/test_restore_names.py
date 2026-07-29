import pytest

from app.restore_names import restore_names


@pytest.fixture
def users_data() -> list[dict]:
    return [
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
            "first_name": "John",
            "last_name": "Doe",
            "full_name": "John Doe",
        },
    ]


@pytest.mark.parametrize(
    "expected",
    [
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
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            },
        ]
    ],
)
def test_restore_names(users_data: list[dict], expected: list[dict]) -> None:
    restore_names(users_data)
    assert users_data == expected, "First names were not restored correctly"
