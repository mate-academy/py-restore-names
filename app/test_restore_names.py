import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_list_w_dict",
    [
        [{"first_name": "Jack", "full_name": "Jack Holy"}],
        [{"full_name": "Jack Holy"}],
        [{"first_name": None, "full_name": "Jack Holy"}]
    ],
    ids=[
        "first_name is ok",
        "no first_name",
        "first_name is None"
    ]
)
def test_restore_names(input_list_w_dict: list) -> None:
    restore_names(input_list_w_dict)
    assert input_list_w_dict[0]["first_name"] == "Jack"
