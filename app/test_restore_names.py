import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,result",
    (
        ({"first_name": None,
          "last_name": "Holy",
          "full_name": "Jack Holy"
          },
         {"first_name": "Jack",
          "last_name": "Holy",
          "full_name": "Jack Holy"}),

        ({"last_name": "Adams",
          "full_name": "Mike Adams"
          },
            {"first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"
             }
         )
    )
)
def test_restore_names(users: list[dict], result: list[dict]) -> None:
    users_temp = users
    restore_names(users_temp)
    assert users_temp == result
