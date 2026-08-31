from app.restore_names import restore_names


class TestRestoreNames:
    def test_restores_missing_first_name_key(self) -> None:
        users = [{"last_name": "Adams", "full_name": "Mike Adams"}]

        restore_names(users)

        assert users[0]["first_name"] == "Mike"

    def test_restores_first_name_when_none(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "Jack"

    def test_does_not_overwrite_existing_first_name(self) -> None:
        users = [
            {
                "first_name": "Nickname",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "Nickname"

    def test_handles_multiple_users_with_mixed_state(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {"last_name": "Adams", "full_name": "Mike Adams"},
            {
                "first_name": "Anna",
                "last_name": "Lee",
                "full_name": "Anna Lee",
            },
        ]

        restore_names(users)

        assert users[0]["first_name"] == "Jack"
        assert users[1]["first_name"] == "Mike"
        assert users[2]["first_name"] == "Anna"

    def test_empty_list_does_not_raise(self) -> None:
        users = []

        restore_names(users)

        assert users == []

    def test_returns_none(self) -> None:
        users = [{"last_name": "Adams", "full_name": "Mike Adams"}]

        result = restore_names(users)

        assert result is None
