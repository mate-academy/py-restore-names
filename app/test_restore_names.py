import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "person",
    [
        [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        ]
    ]
)
def test_restore_names(
        person: list[dict],
) -> None:
    restore_names(person)
    for user in person:
        assert "first_name" in user
        assert user["first_name"] is not None
