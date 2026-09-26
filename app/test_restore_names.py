import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    ("user", "expected_user"),
    [
        pytest.param(
            {"first_name": None, "full_name": "Mike Adams"},
            {"first_name": "Mike", "full_name": "Mike Adams"},
            id="first_name_is_none",
        ),
        pytest.param(
            {"full_name": "Jack Holy"},
            {"first_name": "Jack", "full_name": "Jack Holy"},
            id="only_full_name",
        ),
        pytest.param(
            {"first_name": "Alice", "full_name": "Alice Green"},
            {"first_name": "Alice", "full_name": "Alice Green"},
            id="all_here",
        ),
        pytest.param(
            {"first_name": "", "full_name": "Bob Brown"},
            {"first_name": "", "full_name": "Bob Brown"},
            id="first_name_is_empty_string",
        ),
    ],
)
def test_restore_names_updates_first_name(
    user: dict,
    expected_user: dict,
) -> None:
    users = [user.copy()]

    result = restore_names(users)

    assert result is None
    assert users == [expected_user]
