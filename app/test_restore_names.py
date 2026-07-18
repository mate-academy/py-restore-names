import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, result",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Potter",
                    "full_name": "Harry Potter",
                },
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            [
                {
                    "first_name": "Harry",
                    "last_name": "Potter",
                    "full_name": "Harry Potter",
                },
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
            id="Should add name from full name if name equal to None"
        ),
        pytest.param(
            [
                {
                    "first_name": "Harry",
                    "last_name": "Potter",
                    "full_name": "Harry Potter",
                },
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                }
            ],
            [
                {
                    "first_name": "Harry",
                    "last_name": "Potter",
                    "full_name": "Harry Potter",
                },
                {
                    "first_name": "John",
                    "last_name": "Smith",
                    "full_name": "John Smith",
                }
            ],
            id="Should do nothing if name not None"
        ),
        pytest.param(
            [
                {
                    "last_name": "Holland",
                    "full_name": "Tom Holland",
                },
                {
                    "last_name": "Dorofeeva",
                    "full_name": "Nadiia Dorofeeva",
                }
            ],
            [
                {
                    "first_name": "Tom",
                    "last_name": "Holland",
                    "full_name": "Tom Holland",
                },
                {
                    "first_name": "Nadiia",
                    "last_name": "Dorofeeva",
                    "full_name": "Nadiia Dorofeeva",
                }
            ],
            id="Should return name from full name if name not exist"
        )
    ]
)
def test_func_working_correctly(user: list, result: list) -> None:
    restore_names(user)
    assert user == result
