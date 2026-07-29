import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "check_users, restore_users_name",
    [
        (
            [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy",
              },
             {"last_name": "Adams",
              "full_name": "Mike Adams"
              }],

            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy",
              },
             {"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"
              }]
        ),
    ]
)
def test_restore_names(
        check_users: list[dict],
        restore_users_name: list[dict]
) -> None:
    restore_names(check_users)
    assert check_users == restore_users_name
