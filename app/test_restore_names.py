import pytest
from app.restore_names import restore_names


@pytest.fixture()
def result_template() -> list[dict]:
    return [
        {"first_name": "Jack",
         "last_name": "Holy",
         "full_name": "Jack Holy"}
    ]


def test_f_name_none(result_template: list[dict]) -> None:
    value = [
        {"first_name": None,
         "last_name": "Holy",
         "full_name": "Jack Holy"}
    ]
    restore_names(value)
    assert value == result_template


def test_f_name_missing(result_template: list[dict]) -> None:
    value = [{"last_name": "Holy", "full_name": "Jack Holy"}]
    restore_names(value)
    assert value == result_template
