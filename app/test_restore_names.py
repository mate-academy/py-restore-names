import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):

    def test_restore_name(self, users: list) -> None:
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Jack")
        self.assertEqual(users[1]["first_name"], "Mike")

    def test_restore_name_empty(self, users: list) -> None:
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "")
        self.assertEqual(users[1]["first_name"], "None")
