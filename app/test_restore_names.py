import pytest
from app.restore_names import restore_names


@pytest.fixture()
def users_failed_sample() -> list:
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


@pytest.fixture()
def users_corrected_sample() -> list:
    return [
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


def test_should_perform_primary_goal(
        users_failed_sample: list, users_corrected_sample: list
) -> None:
    restore_names(users_failed_sample)
    assert users_failed_sample == users_corrected_sample


def test_should_return_nothing(users_failed_sample: list) -> None:
    assert restore_names(users_failed_sample) is None
