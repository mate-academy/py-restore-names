import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user_name_broken, user_name_fixed",
    (
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            id="first name None"
        ),
        pytest.param(
            [{
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            }],
            id="dict with cell"
        ),
    )
)
def test_restore_names(user_name_broken: list[dict],
                       user_name_fixed: list[dict]) -> None:

    restore_names(user_name_broken)

    assert user_name_broken == user_name_fixed
