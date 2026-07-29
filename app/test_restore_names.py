import pytest
from app.restore_names import restore_names


@pytest.fixture()
def dictionary() -> list:
    return [{"last_name": "Holy", "full_name": "Jack Holy"}]


def test_restore_names_when_name_is_not_in_dict(dictionary: list) -> None:
    restore_names(dictionary)
    assert dictionary == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


def test_restore_names_when_name_is_none(dictionary: list) -> None:
    dictionary[0]["first_name"] = None
    restore_names(dictionary)
    assert dictionary == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


def test_restore_names_when_dictionary_is_ok(dictionary: list) -> None:
    dictionary[0]["first_name"] = "Jack"
    restore_names(dictionary)
    assert dictionary == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
