from copy import copy

import pytest

from app.restore_names import restore_names


@pytest.fixture()
def john_user_fixture() -> dict[str, str]:
    return {
        "first_name": "John",
        "last_name": "Wick",
        "full_name": "John Wick"
    }


@pytest.fixture()
def bob_user_fixture() -> dict[str, str]:
    return {
        "first_name": "Bob",
        "last_name": "Dylan",
        "full_name": "Bob Dylan"
    }


class TestRestoreNames:

    def test_should_not_change_name_if_already_exists(
            self,
            john_user_fixture: dict[str, str]
    ) -> None:
        john_user_fixture["first_name"] = "Bob"
        john_copy = copy(john_user_fixture)

        restore_names([john_copy])

        assert john_copy == john_user_fixture

    def test_should_set_first_name_from_full_name(
            self,
            john_user_fixture: dict[str, str]
    ) -> None:
        john_copy = copy(john_user_fixture)

        del john_copy["first_name"]
        restore_names([john_copy])
        assert john_copy == john_user_fixture

        john_copy["first_name"] = None
        restore_names([john_copy])
        assert john_copy == john_user_fixture

    def test_should_work_for_users_list(
            self,
            john_user_fixture: dict[str, str],
            bob_user_fixture: dict[str, str]
    ) -> None:
        john_copy = copy(john_user_fixture)
        bob_copy = copy(bob_user_fixture)

        del john_copy["first_name"]
        del bob_copy["first_name"]

        restore_names([john_copy, bob_copy])

        assert john_copy == john_user_fixture
        assert bob_copy == bob_user_fixture

    @pytest.mark.parametrize(
        "users,expected_exception",
        (
            ([{}], KeyError),
            ([{"full_name": 1}], AttributeError)
        ),
        ids=(
            "should raise if `first_name` and `full_name` are not exists",
            "should raise if `full_name` is not str type"
        )
    )
    def test_raise_exceptions(
            self,
            users: list,
            expected_exception: KeyError | AttributeError
    ) -> None:
        with pytest.raises(expected_exception):
            restore_names(users)
