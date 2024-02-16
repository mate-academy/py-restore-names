import pytest
from app.restore_names import restore_names


def test_should_return_none() -> None:
    assert restore_names([]) is None


@pytest.mark.parametrize(
    "users,expected",
    [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, {
            "first_name": None,
            "last_name": "Mosh",
            "full_name": "Max Mosh",
        }, ], [{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, {
            "first_name": "Max",
            "last_name": "Mosh",
            "full_name": "Max Mosh",
        }, ]), ],
)
def test_when_first_name_is_none(users: list[dict],
                                 expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected


@pytest.mark.parametrize(
    "users,expected",
    [
        ([{
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, {
            "last_name": "Mosh",
            "full_name": "Max Mosh",
        }], [{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, {
            "first_name": "Max",
            "last_name": "Mosh",
            "full_name": "Max Mosh",
        }]), ],
)
def test_when_first_name_is_not_exist(users: list[dict],
                                      expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected


@pytest.mark.parametrize(
    "users,expected",
    [
        ([{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, {
            "first_name": "Max",
            "last_name": "Mosh",
            "full_name": "Max Mosh",
        }], [{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }, {
            "first_name": "Max",
            "last_name": "Mosh",
            "full_name": "Max Mosh",
        }]), ],
)
def test_when_all_right(users: list[dict],
                        expected: list[dict]) -> None:
    restore_names(users)
    assert users == expected
