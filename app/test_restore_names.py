import pytest
from app.restore_names import restore_names


@pytest.fixture()
def list_templates() -> list[dict[str, str | None] | dict[str, str]]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]


def test_restore_restore_names(list_templates: list[dict]) -> None:
    answer_template = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(list_templates)
    assert list_templates == answer_template
