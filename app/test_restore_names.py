import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        # 🔹 first_name отсутствует
        (
            [{"last_name": "Holy", "full_name": "Jack Holy"}],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
        ),
        # 🔹 first_name = None
        (
            [{"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"}],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
        ),
        # 🔹 first_name уже есть
        (
            [{"first_name": "Liam", "last_name": "Gray", "full_name": "Liam Gray"}],
            [
                {
                    "first_name": "Liam",
                    "last_name": "Gray",
                    "full_name": "Liam Gray",
                }
            ],
        ),
    ],
)
def test_restore_names(users: list, expected: list) -> None:
    result = restore_names(users)
    assert result is None
    assert users == expected
