import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "first_in, then_out",
    [([{"first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy"},
       {"last_name": "Adams",
        "full_name": "Mike Adams"}],
      [{"first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy"},
       {"first_name": "Mike",
        "last_name": "Adams",
        "full_name": "Mike Adams"}])]
)
def test_restore_names_right(first_in: list[dict],
                             then_out: list[dict]) -> None:
    restore_names(first_in)
    assert first_in[0]["first_name"] == then_out[0]["first_name"]
    assert first_in[1]["first_name"] == then_out[1]["first_name"]
