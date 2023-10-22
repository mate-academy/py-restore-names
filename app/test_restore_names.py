import pytest

from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.fixture()
    def users_with_firstname_as_none(self) -> list:
        return [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": None,
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]

    @pytest.fixture()
    def users_with_no_first_name(self) -> list:
        return [
            {
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]

    def test_users_with_firstname_as_none(
            self,
            users_with_firstname_as_none: list[dict]
    ) -> None:
        restore_names(users_with_firstname_as_none)
        assert users_with_firstname_as_none == [
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

    def test_users_with_no_first_name(
            self,
            users_with_no_first_name: list[dict]
    ) -> None:
        restore_names(users_with_no_first_name)
        assert users_with_no_first_name == [
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
