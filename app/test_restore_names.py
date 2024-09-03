import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user,expected_name",
    [
        ([{"first_name": "Jack",
           "last_name": "Holy",
           "full_name": "Jack Holy"}],
         "Jack"
         ),
        ([{"first_name": None,
           "last_name": "Holy",
           "full_name": "Jack Holy"}],
         "Jack",
         ),
        ([{"last_name": "Holy",
           "full_name": "Jack Holy"}],
         "Jack"
         ),
    ]
)
def test_different_ways(
        user: list[dict],
        expected_name: str
) -> None:
    restore_names(user)
    assert user[0]["first_name"] == expected_name
