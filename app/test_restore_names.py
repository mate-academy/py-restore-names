import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "first_name, last_name, result",
    [
        (None, "Holy", "Jack Holy"),
        (None, "Adams", "Mike Adams"),
    ]
)
def test_restore_names(first_name: str, last_name: str, result: str) -> None:

    users = [
        {
            "first_name": first_name,
            "last_name": last_name,
            "full_name": result},
        {
            "last_name": last_name,
            "full_name": result
        }
    ]
    restore_names(users)
    assert result.split()[0] == users[0]["first_name"]
    assert result.split()[0] == users[1]["first_name"]
