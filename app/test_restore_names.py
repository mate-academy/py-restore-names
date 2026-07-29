import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "param, count",
    [
        (
            [{"first_name": None, "full_name": "Jack Holy"}],
            [{"first_name": "Jack", "full_name": "Jack Holy"}]
        ),
        (
            [{"full_name": "Mike Adams"}],
            [{"first_name": "Mike", "full_name": "Mike Adams"}]
        )
    ],
    ids=[
        "check_none_in_name",
        "check_none_last_name"
    ]
)
def test_restore_names_function(param: list, count: list) -> None:
    restore_names(param)
    assert param == count
