from app.restore_names import restore_names
import unittest


class TestRestoreNames(unittest.TestCase):
    def test_restore_names(self) -> None:

        users = [
            {"full_name": "John Doe", "first_name": None},
            {"full_name": "Alice Smith", "first_name": "Alice"},
            {"full_name": "Bob Johnson"},
        ]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "John")
        self.assertEqual(users[1]["first_name"], "Alice")
        self.assertEqual(users[2]["first_name"], "Bob")
