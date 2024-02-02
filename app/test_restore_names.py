import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "person_template", [
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
def test_restore_names(person_template: list[dict]) -> None:
    restore_names(person_template)
    for user in person_template:
        assert "first_name" in user
        assert user["first_name"] is not None
