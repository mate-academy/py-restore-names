import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        ([
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
        ]
        ),

        ([
            {
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
        ]
        )

    ], ids=[
        "If first_name is 'None' should be get from full_name",
        "If first_name is missing should be get from full_name",
    ]
)
def test_restore_names(users: list[dict], expected: list[dict]) -> None:
    restore_names(users)
    assert expected == users
