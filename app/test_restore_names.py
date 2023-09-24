import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):

    def test_restore_names_with_none_first_name(self) -> None:
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

    def test_restore_names_with_existing_first_name(self) -> None:
        users = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John Doe",
            },
            {
                "last_name": "Smith",
                "full_name": "Alice Smith",
            },
        ]
        restore_names(users)

        self.assertEqual(users[0]["first_name"], "John")
        self.assertEqual(users[1]["first_name"], "Alice")

    def test_restore_names_with_no_full_name(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
            },
            {
                "last_name": "Adams",
            },
        ]
        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Holy")
        self.assertEqual(users[1]["first_name"], "Adams")


if __name__ == '__main__':
    unittest.main()
