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
            {
                "first_name": "Already",
                "last_name": "Present",
                "full_name": "Should Not Change",
            }
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
            {
                "first_name": "Already",
                "last_name": "Present",
                "full_name": "Should Not Change",
            }
        ]

        restore_names(users)
        self.assertEqual(users, expected_users)

    def test_empty_user_list(self) -> None:
        users = []
        restore_names(users)
        self.assertEqual(users, [])

    def test_no_full_name_field(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Smith",
            }
        ]
        with self.assertRaises(KeyError):
            restore_names(users)

    def test_full_name_with_multiple_names(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Van Rossum",
                "full_name": "Guido Van Rossum",
            }
        ]
        expected_users = [
            {
                "first_name": "Guido",
                "last_name": "Van Rossum",
                "full_name": "Guido Van Rossum",
            }
        ]
        restore_names(users)
        self.assertEqual(users, expected_users)
