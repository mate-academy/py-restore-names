import pytest

from app.main import restore_names


class TestRestoreNames:
    def test_should_restore_first_name_when_none(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "Jack"

    def test_should_restore_first_name_when_key_is_missing(self) -> None:
        users = [
            {"last_name": "Adams", "full_name": "Mike Adams"},
        ]

        restore_names(users)

        assert users[0]["first_name"] == "Mike"

    def test_should_not_change_existing_first_name(self) -> None:
        users = [
            {
                "first_name": "John",
                "last_name": "Smith",
                "full_name": "Johnny Smith",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "John"

    def test_should_restore_first_name_with_middle_name(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John Michael Doe",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "John"

    def test_should_restore_names_for_multiple_users(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {"last_name": "Adams", "full_name": "Mike Adams"},
        ]

        restore_names(users)

        assert users == [
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

    def test_should_not_mix_up_names_between_users(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Anna",
                "last_name": "Petrova",
                "full_name": "Anna Petrova",
            },
            {"last_name": "Adams", "full_name": "Mike Adams"},
        ]

        restore_names(users)

        first_names = [user["first_name"] for user in users]
        assert first_names == ["Jack", "Anna", "Mike"]

    def test_should_handle_empty_list(self) -> None:
        users: list[dict] = []

        restore_names(users)

        assert users == []

    def test_should_return_none(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]

        result = restore_names(users)

        assert result is None

    @pytest.mark.parametrize(
        "user, expected_first_name",
        [
            (
                {"first_name": None, "full_name": "Jack Holy"},
                "Jack",
            ),
            (
                {"full_name": "Mike Adams"},
                "Mike",
            ),
            (
                {"first_name": "", "full_name": "Anna Petrova"},
                "",
            ),
        ],
    )
    def test_should_restore_only_when_missing_or_none(
        self,
        user: dict,
        expected_first_name: str,
    ) -> None:
        users = [user]

        restore_names(users)

        assert users[0]["first_name"] == expected_first_name
