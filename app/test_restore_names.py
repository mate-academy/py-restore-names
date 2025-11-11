import pytest
from app.restore_names import restore_names


@pytest.fixture()
def dict_template() -> list:
    return [
        {
        "full_name": None
        }
    ]


def test_restore_names_raise_exception(dict_template) -> None:
    with pytest.raises(AttributeError):
        restore_names(dict_template)


@pytest.mark.parametrize(
    "dict_template, expected",
    [
        ([{"full_name": "Peter Metr"}], [{"full_name": "Peter Metr", "first_name": "Peter"}]),
        ([{"full_name": "Peter Metr", "first_name": "Peter"}], [{"full_name": "Peter Metr", "first_name": "Peter"}]),
        ([{"full_name": "Peter Metr", "first_name": None}], [{"full_name": "Peter Metr", "first_name": "Peter"}]),
    ]
)
def test_restore_names(dict_template, expected) -> None:
    restore_names(dict_template)
    assert dict_template == expected
