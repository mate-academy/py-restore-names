import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, result",
    [
        ([{
            "first_name": None,
            "last_name": "Constantine",
            "full_name": "John Constantine",
        }], [{
            "first_name": "John",
            "last_name": "Constantine",
            "full_name": "John Constantine",
        }]),
        ([{
            "last_name": "Christy",
            "full_name": "Agatha Christy",
        }], [{
            "first_name": "Agatha",
            "last_name": "Christy",
            "full_name": "Agatha Christy",
        }])
    ]
)
def test_should_restore_names(
        users: list[dict],
        result: list[dict],
) -> None:
    restore_names(users)
    assert users == result
