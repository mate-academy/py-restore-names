from typing import Any

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "first_name,full_name,result",
    [
        (None, "Jack Holy", "Jack"),
        (False, "Mike Adams", "Mike")
    ],
    ids=[
        "None",
        "Not existing"
    ]
)
def test_successfully_restored_names(
    first_name: Any,
    full_name: str,
    result: str
) -> None:
    users = [{
        "first_name": first_name,
        "last_name": full_name.split()[1],
        "full_name": full_name
    }]
    if not users[0].get("first_name"):
        del users[0]["first_name"]
    result = [{
        "first_name": full_name.split()[0],
        "last_name": full_name.split()[1],
        "full_name": full_name
    }]
    restore_names(users)
    assert (
        users == result
    ), "Result is not as expected"


def test_key_error() -> None:
    users = [{
        "first_name": None,
        "last_name": "Test"
    }]
    with pytest.raises(KeyError):
        restore_names(users)
