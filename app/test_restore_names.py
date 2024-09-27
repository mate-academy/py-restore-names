import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):

    def test_restore_names_with_none(self) -> None:
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
        expected = [
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
        self.assertEqual(users, expected)

    def test_no_change_needed(self) -> None:
        users = [
            {
                "first_name": "Alice",
                "last_name": "Smith",
                "full_name": "Alice Smith",
            },
            {
                "first_name": "Bob",
                "last_name": "Brown",
                "full_name": "Bob Brown",
            },
        ]
        restore_names(users)
        expected = users.copy()
        self.assertEqual(users, expected)

    def test_multiple_users_with_missing_first_name(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John Doe",
            },
            {
                "first_name": None,
                "last_name": "Johnson",
                "full_name": "Jane Johnson",
            },
        ]
        restore_names(users)
        expected = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            },
            {
                "first_name": "Jane",
                "last_name": "Johnson",
                "full_name": "Jane Johnson",
            },
        ]
        self.assertEqual(users, expected)

    def test_partial_data(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Brown",
                "full_name": "Chris Brown",
            },
            {
                "last_name": "Gray",
                "full_name": "Sam Gray",
            },
            {
                "first_name": "Charlie",
                "last_name": "Green",
                "full_name": "Charlie Green",
            },
        ]
        restore_names(users)
        expected = [
            {
                "first_name": "Chris",
                "last_name": "Brown",
                "full_name": "Chris Brown",
            },
            {
                "first_name": "Sam",
                "last_name": "Gray",
                "full_name": "Sam Gray",
            },
            {
                "first_name": "Charlie",
                "last_name": "Green",
                "full_name": "Charlie Green",
            },
        ]
        self.assertEqual(users, expected)
