from typing import List
import pytest

from app.restore_names import restore_names


@pytest.fixture()
def users_expected_template() -> List[dict]:
    users_expected = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    yield users_expected
    print("test finished")


def test_restore_names_if_first_name_is_none(
        users_expected_template: List[dict]
) -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users=users)
    assert (
        users == users_expected_template
    )


def test_restore_names_if_first_name_is_absent(
    users_expected_template: List[dict]
) -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
    ]
    restore_names(users=users)
    assert (
        users == users_expected_template
    )
