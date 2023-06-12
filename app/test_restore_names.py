import pytest

from app.restore_names import restore_names

from typing import List


@pytest.fixture()
def test_user_template_example_1() -> List[dict]:
    return [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


@pytest.fixture()
def test_user_template_example_2() -> List[dict]:
    return [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]


def test_first_name_is_none(
        test_user_template_example_1: List[dict]
) -> None:
    test_user_template_example_1[0]["first_name"] = None
    restore_names(test_user_template_example_1)
    assert test_user_template_example_1 == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]


def test_first_name_is_absent(
        test_user_template_example_2: List[dict]
) -> None:
    test_user_template_example_2[0].pop("first_name")
    restore_names(test_user_template_example_2)
    assert test_user_template_example_2 == [
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
