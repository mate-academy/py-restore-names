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
            [{"full_name": "Jack Holy"}],
            [{"first_name": "Jack", "full_name": "Jack Holy"}]
        )
    ],
    ids=[
        "Check without first name",
        "Check without last_name"
    ]
)
def test_restore_names(param: list, count: list) -> None:
    restore_names(param)
    assert param == count
