import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "data, result",
    [
        (
            [{"first_name": None, "last_name": "Holy",
              "full_name": "Jack Holy"}],
            [{"first_name": "Jack", "last_name": "Holy",
              "full_name": "Jack Holy"}],
        ),
        (
            [{"last_name": "Adams", "full_name":
                "Mike Adams"}],
            [{"first_name": "Mike", "last_name": "Adams",
              "full_name": "Mike Adams"}],
        ),
        (
            [{"first_name": "John", "last_name": "Doe",
              "full_name": "John Doe"}],
            [{"first_name": "John", "last_name": "Doe",
              "full_name": "John Doe"}],
        ),
    ],
)
def test_restore_names(data: list, result: list) -> None:
    assert restore_names(data) is None
    assert data == result
