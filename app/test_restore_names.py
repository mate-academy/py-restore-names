import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):
    def test_restore_missing_first_name(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John Doe"
            },
            {
                "last_name": "Smith",
                "full_name": "Jane Smith"
            }
        ]
        expected = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe"
            },
            {
                "first_name": "Jane",
                "last_name": "Smith",
                "full_name": "Jane Smith"
            }
        ]
        restore_names(users)
        self.assertEqual(users, expected)

    def test_no_change_when_first_name_present(self) -> None:
        users = [
            {
                "first_name": "Alice",
                "last_name": "Brown",
                "full_name": "Alice Brown"
            },
            {
                "first_name": "Bob",
                "last_name": "Miller",
                "full_name": "Bob Miller"
            }
        ]
        expected = users.copy()
        restore_names(users)
        self.assertEqual(users, expected)

    def test_mixed_users(self) -> None:
        users = [
            {
                "first_name": "Ann",
                "last_name": "Jones",
                "full_name": "Ann Jones"
            },
            {
                "first_name": None,
                "last_name": "Kent",
                "full_name": "Clark Kent"
            },
            {
                "last_name": "Wayne",
                "full_name": "Bruce Wayne"
            }
        ]
        expected = [
            {
                "first_name": "Ann",
                "last_name": "Jones",
                "full_name": "Ann Jones"
            },
            {
                "first_name": "Clark",
                "last_name": "Kent",
                "full_name": "Clark Kent"
            },
            {
                "first_name": "Bruce",
                "last_name": "Wayne",
                "full_name": "Bruce Wayne"
            }
        ]
        restore_names(users)
        self.assertEqual(users, expected)

    def test_empty_list(self) -> None:
        users = []
        expected = []
        restore_names(users)
        self.assertEqual(users, expected)


if __name__ == "__main__":
    unittest.main()
