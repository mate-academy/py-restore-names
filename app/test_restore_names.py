
from app.restore_names import restore_names

import unittest


class TestRestoreNames(unittest.TestCase):

    def test_restore_first_name_none(self) -> None:
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
        expected_users = [
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
        self.assertEqual(users, expected_users)

    def test_restore_first_name_missing(self) -> None:
        users = [
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
        expected_users = [
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
        self.assertEqual(users, expected_users)

    def test_no_change_first_name_exists(self) -> None:
        users = [
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
        expected_users = [
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
        self.assertEqual(users, expected_users)

    def test_empty_list(self) -> None:
        users = []
        expected_users = []
        restore_names(users)
        self.assertEqual(users, expected_users)

    def test_restore_partial_users(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Anna",
                "last_name": "Smith",
                "full_name": "Anna Smith",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
        expected_users = [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": "Anna",
                "last_name": "Smith",
                "full_name": "Anna Smith",
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
        restore_names(users)
        self.assertEqual(users, expected_users)


if __name__ == "__main__":
    unittest.main()
