import unittest
from app.restore_names import restore_names
from typing import List, Dict


class TestRestoreNames(unittest.TestCase):
    def test_restore_missing_first_name(self) -> None:
        users: List[Dict[str, str]] = [
            {"full_name": "Alice Johnson", "first_name": None},
            {"full_name": "Bob Smith"},
            {"full_name": "Charlie Day", "first_name": "Charlie"}
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Alice")
        self.assertEqual(users[1]["first_name"], "Bob")
        self.assertEqual(users[2]["first_name"], "Charlie")

    def test_all_users_have_first_name(self) -> None:
        users: List[Dict[str, str]] = [
            {"full_name": "Diana Prince", "first_name": "Diana"},
            {"full_name": "Clark Kent", "first_name": "Clark"}
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Diana")
        self.assertEqual(users[1]["first_name"], "Clark")

    def test_empty_list(self) -> None:
        users: List[Dict[str, str]] = []
        restore_names(users)
        self.assertEqual(users, [])


if __name__ == "__main__":
    unittest.main()
