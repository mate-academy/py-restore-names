from app.restore_names import restore_names


class TestRestoreNames:
    def test_restores_first_name_when_none(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == "Jack"

    def test_restores_first_name_when_missing(self) -> None:
        users = [
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == "Mike"

    def test_does_not_change_existing_first_name(self) -> None:
        users = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == "John"

    def test_returns_none(self) -> None:
        assert restore_names([]) is None

    def test_handles_multiple_users(self) -> None:
        users = [
            {"first_name": None, "last_name": "A", "full_name": "Tom A"},
            {"last_name": "B", "full_name": "Ann B"},
            {"first_name": "Sam", "last_name": "C", "full_name": "Sam C"},
        ]
        restore_names(users)
        assert users[0]["first_name"] == "Tom"
        assert users[1]["first_name"] == "Ann"
        assert users[2]["first_name"] == "Sam"
