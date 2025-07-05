import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):
    def test_missing_first_name(self) -> None:
        users = [{"full_name": "John Doe"}]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "John")

    def test_first_name_is_none(self) -> None:
        users = [{"full_name": "Jane Smith", "first_name": None}]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Jane")

    def test_first_name_already_present(self) -> None:
        users = [{"full_name": "Alice Johnson", "first_name": "Alice"}]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Alice")

    def test_multiple_users(self) -> None:
        users = [
            {"full_name": "Tom Hardy"},
            {"full_name": "Emma Stone", "first_name": None},
            {"full_name": "Chris Evans", "first_name": "Chris"},
        ]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Tom")
        self.assertEqual(users[1]["first_name"], "Emma")
        self.assertEqual(users[2]["first_name"], "Chris")

    def test_single_word_full_name(self) -> None:
        users = [{"full_name": "Madonna"}]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Madonna")
