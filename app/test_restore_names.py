import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):
    def test_restore_names(self) -> None:
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
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Jack")
        self.assertEqual(users[1]["first_name"], "Mike")

        self.assertEqual(users[0]["last_name"], "Holy")
        self.assertEqual(users[0]["full_name"], "Jack Holy")
        self.assertEqual(users[1]["last_name"], "Adams")
        self.assertEqual(users[1]["full_name"], "Mike Adams")

    def test_restore_names_empty_users(self) -> None:
        users = []
        restore_names(users)
        self.assertEqual(users, [])
