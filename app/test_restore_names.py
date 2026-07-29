import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.fixture()
    def users_with_none_as_firstname(self) -> list:
        return [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]

    @pytest.fixture()
    def users_dont_have_firstname(self) -> list:
        return [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]

    def test_user_has_none_as_first_name(
            self,
            users_with_none_as_firstname: list[dict]
    ) -> None:
        restore_names(users_with_none_as_firstname)
        assert users_with_none_as_firstname == [
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

    def test_user_dont_have_first_name(
            self,
            users_dont_have_firstname: list[dict]
    ) -> None:
        restore_names(users_dont_have_firstname)
        assert users_dont_have_firstname == [
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
