import pytest

from app.restore_names import restore_names


@pytest.fixture()
def dict_template() -> list:
    return [{"last_name": "Holy",
             "full_name": "Jack Holy"
             }]


def test_first_name_not_in_dict(dict_template: list) -> None:
    restore_names(dict_template)
    assert dict_template == [{"first_name": "Jack",
                              "last_name": "Holy",
                              "full_name": "Jack Holy"
                              }]


def test_first_name_is_none(dict_template: list) -> None:
    dict_template[0]["first_name"] = None
    restore_names(dict_template)
    assert dict_template == [{"first_name": "Jack",
                              "last_name": "Holy",
                              "full_name": "Jack Holy"
                              }]
