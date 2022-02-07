from app.restore_names import restore_names
import pytest


@pytest.mark.parametrize(
    "initial,expected",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            "Jack"
        ),
        (
            [
                {
                    "last_name": "Smith",
                    "full_name": "John Smith",
                }
            ],
            "John"
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Vader",
                    "full_name": "Darth Vader",
                }
            ],
            "Darth"
        )
    ]
)
def test_is_firstname_correct(initial, expected):
    restore_names(initial)

    assert initial[0]["first_name"]== expected
