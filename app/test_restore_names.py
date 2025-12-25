import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_without_first_name() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
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
        ]
    ],
    ids=["users without first name"]
)
def test_restore_names(
    users_without_first_name: list[dict],
    expected: list[dict]
) -> None:
    restore_names(users_without_first_name)
    assert (
        users_without_first_name == expected
    ), f"Users first names should be: {expected}"
