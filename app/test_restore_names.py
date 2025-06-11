import pytest
from typing import Type
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "test_user, valid_expected",
    [
        ({"first_name": None, "full_name": "John Smith"}, "John"),
        ({"first_name": "John", "full_name": "John Smith"}, "John"),
        ({"first_name": None, "full_name": "Madonna"}, "Madonna"),
        ({"first_name": None, "full_name": "James Tiberius Kirk"}, "James"),
        (
            {"first_name": None, "full_name": "Anne-Marie O'Neill"},
            "Anne-Marie"
        ),
        ({"full_name": "Alice Johnson"}, "Alice"),
    ]
)
def test_restore_names_valid(test_user: dict, valid_expected: str) -> None:
    copy_user = [test_user.copy()]
    restore_names(copy_user)
    assert copy_user[0]["first_name"] == valid_expected


@pytest.mark.parametrize(
    "test_user_invalid, invalid_expected",
    [
        ({"first_name": None, "full_name": None}, AttributeError),
        ({"first_name": None}, KeyError)
    ]
)
def test_restore_names_invalid(
        test_user_invalid: dict,
        invalid_expected: Type[BaseException]
) -> None:
    copy_user_invalid = [test_user_invalid.copy()]
    with pytest.raises(invalid_expected):
        restore_names(copy_user_invalid)
