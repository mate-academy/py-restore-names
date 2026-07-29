# test_restore_names.py
import unittest
from typing import List
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):
    def test_restore_missing_first_name(self) -> None:
        """Test restoring first_name when it's missing."""
        users: List[dict] = [
            {
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": None,
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
        expected: List[dict] = [
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
        restore_names(users)
        self.assertEqual(users, expected)

    def test_no_change_when_first_name_present(self) -> None:
        """Test that first_name remains unchanged when present."""
        users: List[dict] = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            },
        ]
        expected: List[dict] = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            },
        ]
        restore_names(users)
        self.assertEqual(users, expected)

    def test_empty_users_list(self) -> None:
        """Test that an empty users list remains unchanged."""
        users: List[dict] = []
        expected: List[dict] = []
        restore_names(users)
        self.assertEqual(users, expected)

    def test_no_full_name_raises_key_error(self) -> None:
        """Test that a KeyError is raised when full_name missing."""
        users: List[dict] = [
            {
                "first_name": None,
                "last_name": "Smith",
            },
        ]
        with self.assertRaises(KeyError):
            restore_names(users)


if __name__ == "__main__":
    unittest.main()
