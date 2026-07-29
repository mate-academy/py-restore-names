import pytest
from app.restore_names import restore_names


def test_restore_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]

    restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[0]["last_name"] == "Holy"
    assert users[0]["full_name"] == "Jack Holy"

    assert users[1]["first_name"] == "Mike"
    assert users[1]["last_name"] == "Adams"
    assert users[1]["full_name"] == "Mike Adams"


if __name__ == "__main__":
    pytest.main()
