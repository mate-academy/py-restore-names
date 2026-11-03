import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users,expected",
    [
        pytest.param(
            {
                "last_name": "Black",
                "full_name": "Jack Black"
            }, "Jack",
            id="test function should set name if name absent"
        ),
        pytest.param(
            {
                "first_name": None,
                "last_name": "Montana",
                "full_name": "Tony Montana"}, "Tony",
            id="test function should set name if name is None"
        ),
        pytest.param(
            {
                "first_name": "John",
                "last_name": "Marston",
                "full_name": "John Marston"}, "John",
            id="test function should do nothing"
        )
    ]

)
def test_restore_names(users: dict, expected: str) -> None:
    restore_names([users])
    assert users["first_name"] == expected


def test_function_should_return_None() -> None:
    assert restore_names([]) is None
