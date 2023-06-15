import pytest
from app.restore_names import restore_names
from typing import List


@pytest.fixture()
def expected_user_output() -> List[dict]:
    return [
        {
            "first_name": "Andriy",
            "last_name": "Sydorenko",
            "full_name": "Andriy Sydorenko"
        }
    ]


@pytest.mark.parametrize(
    "users",
    [
        [{"last_name": "Sydorenko",
          "full_name": "Andriy Sydorenko"}],

        [{"first_name": None,
          "last_name": "Sydorenko",
          "full_name": "Andriy Sydorenko"}],
    ]
)
def test_restores_names_correctly(users: List[dict],
                                  expected_user_output: List[dict]) -> None:
    restore_names(users)
    assert users == expected_user_output
