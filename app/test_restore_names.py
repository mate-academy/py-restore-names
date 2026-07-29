import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "first_name, full_name",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                },
            ],
        )
    ]
)
def test_restore_names(
        first_name: dict,
        full_name: dict
) -> None:
    restore_names(first_name)
    assert first_name == full_name
