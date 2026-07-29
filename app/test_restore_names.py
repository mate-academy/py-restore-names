from app.restore_names import restore_names


class TestRestoreNames:
    def test_restore_names_should_have_key_first_name(self) -> None:
        users = [
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
        restore_names(users)
        assert "first_name" in users[0].keys()

    def test_restore_names_first_name_should_not_be_none(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
        restore_names(users)
        assert users[0]["first_name"] is not None

    def test_restore_names_valid_first_name_should_not_be_changed(self) \
            -> None:
        users = [
            {
                "first_name": "Miki",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
        copy_users = users.copy()
        restore_names(users)
        assert users[0]["first_name"] == copy_users[0]["first_name"]
