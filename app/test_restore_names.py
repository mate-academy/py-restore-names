import pytest

from app.restore_names import restore_names


correct_list = [
    {
        "first_name": "John",
        "last_name": "Smith",
        "full_name": "John Smith"
    }
]


@pytest.fixture()
def persons_template() -> list:
    return [
        {
            "last_name": "Smith",
            "full_name": "John Smith"
        }
    ]


def test_should_add_the_first_name(
        persons_template: list[dict]
) -> None:
    restore_names(persons_template)
    assert persons_template == correct_list


def test_restore_the_first_name_if_value_is_none(
        persons_template: list[dict]
) -> None:
    person = persons_template
    person[0]["first_name"] = None
    restore_names(persons_template)
    assert persons_template == correct_list
