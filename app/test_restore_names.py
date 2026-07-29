import pytest
from app.restore_names import restore_names


def test_restore_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Jefferson",
            "full_name": "Tomas Jefferson",
        },
        {
            "last_name": "Washington",
            "full_name": "George Washington",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Tomas"
    assert users[0]["last_name"] == "Jefferson"
    assert users[0]["full_name"] == "Tomas Jefferson"

    assert users[1]["first_name"] == "George"
    assert users[1]["last_name"] == "Washington"
    assert users[1]["full_name"] == "George Washington"


if __name__ == "main":
    pytest.main()
