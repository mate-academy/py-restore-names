import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):
    def test_restore_missing_first_name(self) -> None:
        users = [
            {"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"
             },
            {"last_name": "Adams",
             "full_name": "Mike Adams"
             },
        ]
        expected = [
            {"first_name": "Jack",
             "last_name": "Holy",
             "full_name": "Jack Holy"
             },
            {"first_name": "Mike",
             "last_name": "Adams",
             "full_name": "Mike Adams"
             },
        ]
        restore_names(users)
        self.assertEqual(users, expected)

    def test_no_missing_first_name(self) -> None:
        users = [
            {"first_name": "Anna",
             "last_name": "Smith",
             "full_name": "Anna Smith"
             },
            {"first_name": "John",
             "last_name": "Doe",
             "full_name": "John Doe"
             },
        ]
        expected = [
            {"first_name": "Anna",
             "last_name": "Smith",
             "full_name": "Anna Smith"
             },
            {"first_name": "John",
             "last_name": "Doe",
             "full_name": "John Doe"
             },
        ]
        restore_names(users)
        self.assertEqual(users, expected)

    def test_mixed_cases(self) -> None:
        users = [
            {"first_name": None,
             "last_name": "Brown",
             "full_name": "Emily Brown"
             },
            {"first_name": "Chris",
             "last_name": "Evans",
             "full_name": "Chris Evans"
             },
            {"last_name": "Johnson",
             "full_name": "Emma Johnson"
             },
        ]
        expected = [
            {"first_name": "Emily",
             "last_name": "Brown",
             "full_name": "Emily Brown"
             },
            {"first_name": "Chris",
             "last_name": "Evans",
             "full_name": "Chris Evans"
             },
            {"first_name": "Emma",
             "last_name": "Johnson",
             "full_name": "Emma Johnson"
             },
        ]
        restore_names(users)
        self.assertEqual(users, expected)

    def test_empty_users(self) -> None:
        users = []
        expected = []
        restore_names(users)
        self.assertEqual(users, expected)


if __name__ == "__main__":
    unittest.main()
