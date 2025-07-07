import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_user, result",
    [
        (
            [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
        ),
        (
            [{"last_name": "Holy",
              "full_name": "Jack Holy"}],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
        ),
        (
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
            [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"}],
        ),
    ],
)
def test_restore_names(list_user: list, result: list) -> None:
    restore_names(list_user)
    assert list_user == result
