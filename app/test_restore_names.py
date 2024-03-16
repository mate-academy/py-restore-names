import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "dict_human,expected_string", [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"}],
         [{"first_name": "Jack",
           "last_name": "Holy",
           "full_name": "Jack Holy"}]),
        ([{
            "last_name": "Black",
            "full_name": "Mike Black"}],
         [{"first_name": "Mike",
           "last_name": "Black",
           "full_name": "Mike Black"}]),
    ]
)
def test_restore_names(
        dict_human: dict,
        expected_string: dict) -> None:
    restore_names(dict_human)
    assert dict_human == expected_string
