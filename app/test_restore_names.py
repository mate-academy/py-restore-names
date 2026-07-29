from typing import Dict

import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected",
    [
        (
            {
                "first_name": None,
                "last_name": "Sparrow",
                "full_name": "Jack Sparrow"
            },
            "Jack",
        ),
        (
            {
                "last_name": "Swann",
                "full_name": "Elizabeth Swann"
            },
            "Elizabeth",
        ),
        (
            {
                "first_name": "Will",
                "last_name": "Turner",
                "full_name": "Will Turner"
            },
            "Will",
        ),
    ],
)
def test_restore_when_first_name_is_missing_or_none(
    user: Dict[str, str | None],
    expected: str
) -> None:
    restore_names([user])
    assert user["first_name"] == expected


def test_restore_first_name_from_full_name_with_spaces() -> None:
    user: Dict[str, str | None] = {
        "first_name": None,
        "last_name": "Barbossa",
        "full_name": "   Hector   Barbossa   "
    }
    restore_names([user])
    assert user["first_name"] == "Hector"


@pytest.mark.parametrize(
    "user",
    [
        {
            "first_name": None,
            "last_name": "Kraken"
            # no full_name
        },
        {
            "first_name": None,
            "last_name": "Jones",
            "full_name": None
        },
        {
            "first_name": None,
            "full_name": 123
        },
    ],
)
def test_restore_raises_on_invalid_full_name(
    user: Dict
) -> None:
    expected_exceptions: tuple[type[BaseException], ...] = (
        KeyError,
        AttributeError,
        TypeError,
    )
    with pytest.raises(expected_exceptions):
        restore_names([user])
