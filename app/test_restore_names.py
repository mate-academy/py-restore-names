import pytest
from .restore_names import restore_names


@pytest.mark.parametrize(
    "users_name,restore_users_name",
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
        )
    ]
)
def test_restore_names(
        users_name: list[dict],
        restore_users_name: list[dict]
) -> None:
    restore_names(users_name)
    assert users_name == restore_users_name
