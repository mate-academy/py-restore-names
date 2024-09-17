import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_result",
    [
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            "Jack",
            id="first name should be Jack"
        ),
        pytest.param(
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            "Mike",
            id="Should be Mike"
        ),
        pytest.param(
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack111 Holy",
            }],
            "Jack",
            id="Should NOT change first name"
        )
    ]
)
def test_restore_names(users, expected_result):
    restore_names(users)
    for i in range(len(users)):
        assert users[i]["first_name"] == expected_result
