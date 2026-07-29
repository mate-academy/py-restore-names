import pytest

from app.restore_names import restore_names


@pytest.fixture()
def persons_without_first_name() -> list[dict]:
    return [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


@pytest.fixture()
def persons_with_full_info() -> list[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]


def test_function_was_done(
        persons_without_first_name: list[dict],
        persons_with_full_info: list[dict]
) -> None:
    restore_names(persons_without_first_name)
    assert persons_without_first_name == persons_with_full_info
