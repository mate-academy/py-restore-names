import unittest

from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):
    def test_restore_with_none_first_name(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Jack")

    def test_restore_with_missing_first_name(self) -> None:
        users = [
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        ]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Mike")

    def test_first_name_already_present(self) -> None:
        users = [
            {
                "first_name": "Anna",
                "last_name": "Smith",
                "full_name": "Anna Smith",
            }
        ]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Anna")

    def test_multiple_users(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Sara",
                "last_name": "Jones",
                "full_name": "Sara Jones",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        ]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Jack")
        self.assertEqual(users[1]["first_name"], "Sara")
        self.assertEqual(users[2]["first_name"], "Mike")
