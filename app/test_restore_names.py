import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected",
    [
        pytest.param(
            [{"first_name": None, "full_name": "Jack Holy"}],
            "Jack",
            id="None value for first_name"
        ),
        pytest.param(
            [{"last_name": "Adams", "full_name": "Mike Adams"}],
            "Mike",
            id="Without first_name value"
        ),
        pytest.param(
            [{"first_name": "Simon", "full_name": "Simon Smith"}],
            "Simon",
            id="No changes"
        )
    ]
)
def test_restore_names(user: list[dict], expected: str) -> None:
    restore_names(user)
    assert user[0]["first_name"] == expected
