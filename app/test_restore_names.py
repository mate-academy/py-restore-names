import pytest
from app.restore_names import restore_names


@pytest.fixture(scope="function")
def users() -> list:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Test",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Jessy",
            "full_name": "Mark Jessy"
        },

    ]
    return users


MISSING = "missing"


@pytest.mark.parametrize(
    "inx, before_first, after_first",
    [
        (0, None, "Jack"),
        (1, MISSING, "Jack"),
        (2, "Test", "Test"),
        (3, MISSING, "Mark")
    ],
    ids=[
        "first name is none",
        "first name is missing",
        "first name is the same as before",
        "first name is first part of the full name"
    ]
)
def test_restore_names(
        users: list,
        inx: int,
        before_first: str,
        after_first: str
) -> None:
    if before_first == MISSING:
        assert "first_name" not in users[inx]
    elif before_first is None:
        assert users[inx]["first_name"] is None
    else:
        assert users[inx]["first_name"] == before_first

    restore_names(users)
    assert users[inx]["first_name"] == after_first
    if inx == 3:
        assert users[inx]["first_name"] == users[inx]["full_name"].split()[0]
