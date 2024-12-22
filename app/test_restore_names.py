import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):

    def test_restore_first_name_when_none(self) -> None:
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

    def test_restore_first_name_when_missing(self) -> None:
        users = [
            {
                "last_name": "Smith",
                "full_name": "John Smith",
            },
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "Jane Doe",
            },
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "John")
        self.assertEqual(users[1]["first_name"], "Jane")

    def test_no_change_when_first_name_present(self) -> None:
        users = [
            {
                "first_name": "Alice",
                "last_name": "Wonderland",
                "full_name": "Alice Wonderland",
            },
            {
                "first_name": "Bob",
                "last_name": "Builder",
                "full_name": "Bob Builder",
            },
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Alice")
        self.assertEqual(users[1]["first_name"], "Bob")

    def test_empty_user_list(self) -> None:
        users = []

        restore_names(users)

        self.assertEqual(users, [])

    def test_restore_first_name_for_multiple_words_in_full_name(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Smith",
                "full_name": "John Michael Smith",
            },
            {
                "first_name": None,
                "last_name": "Brown",
                "full_name": "Sara Lee Brown",
            },
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "John")
        self.assertEqual(users[1]["first_name"], "Sara")


if __name__ == "__main__":
    unittest.main()
