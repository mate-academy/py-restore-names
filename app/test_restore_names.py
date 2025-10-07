from app.restore_names import restore_names


class TestRestoreNames:
    def test_restore_first_name_when_none(self) -> None:
        """Test restoring first_name when it's None"""
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == "Jack"

    def test_restore_first_name_when_missing(self) -> None:
        """Test restoring first_name when the field is missing"""
        users = [
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == "Mike"

    def test_preserve_existing_first_name(self) -> None:
        """Test that existing first_name is not overwritten"""
        users = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "Jonathan Doe",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == "John"

    def test_empty_list(self) -> None:
        """Test with an empty list of users"""
        users = []
        restore_names(users)
        assert users == []

    def test_multiple_users_mixed_conditions(self) -> None:
        """Test with multiple users having different conditions"""
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
            {
                "first_name": "Sarah",
                "last_name": "Connor",
                "full_name": "Sarah Connor",
            },
        ]
        restore_names(users)
        assert users[0]["first_name"] == "Jack"
        assert users[1]["first_name"] == "Mike"
        assert users[2]["first_name"] == "Sarah"

    def test_full_name_with_multiple_parts(self) -> None:
        """Test with full_name containing multiple parts (middle names)"""
        users = [
            {
                "first_name": None,
                "last_name": "Kennedy",
                "full_name": "John Fitzgerald Kennedy",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == "John"

    def test_full_name_with_single_word(self) -> None:
        """Test with full_name containing only one word"""
        users = [
            {
                "first_name": None,
                "last_name": "",
                "full_name": "Madonna",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == "Madonna"

    def test_modifies_list_in_place(self) -> None:
        """Test that the function modifies the list in place"""
        users = [
            {
                "first_name": None,
                "last_name": "Smith",
                "full_name": "Alice Smith",
            }
        ]
        original_list = users
        restore_names(users)
        assert users is original_list
        assert users[0]["first_name"] == "Alice"

    def test_empty_string_first_name_is_preserved(self) -> None:
        """Test that empty string first_name is preserved (not None)"""
        users = [
            {
                "first_name": "",
                "last_name": "Brown",
                "full_name": "Charlie Brown",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == ""

    def test_all_users_have_valid_first_names(self) -> None:
        """Test with all users having valid first_names"""
        users = [
            {
                "first_name": "Tom",
                "last_name": "Hanks",
                "full_name": "Thomas Hanks",
            },
            {
                "first_name": "Emma",
                "last_name": "Watson",
                "full_name": "Emma Charlotte Watson",
            },
        ]
        restore_names(users)
        assert users[0]["first_name"] == "Tom"
        assert users[1]["first_name"] == "Emma"

    def test_first_name_with_special_characters(self) -> None:
        """Test with full_name containing special characters"""
        users = [
            {
                "first_name": None,
                "last_name": "O'Brien",
                "full_name": "Patrick O'Brien",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == "Patrick"

    def test_first_name_zero_value(self) -> None:
        """Test that numeric zero is preserved (truthy check)"""
        users = [
            {
                "first_name": 0,
                "last_name": "Test",
                "full_name": "Zero Test",
            }
        ]
        restore_names(users)
        assert users[0]["first_name"] == 0
