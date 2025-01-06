import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):

    def test_restore_names(self):
        users = [
            {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
            {"last_name": "Adams", "full_name": "Mike Adams"},
            {"first_name": "Sarah", "last_name": "Williams", "full_name": "Sarah Williams"},
            {"first_name": None, "last_name": "Taylor", "full_name": "James Taylor"}
        ]

        restore_names(users)

        self.assertEqual(users[0]["first_name"], "Jack")
        self.assertEqual(users[1]["first_name"], "Mike")
        self.assertEqual(users[2]["first_name"], "Sarah")
        self.assertEqual(users[3]["first_name"], "James")

    def test_empty_list(self):
        users = []
        restore_names(users)
        self.assertEqual(users, [])

    def test_no_first_name_and_full_name(self):
        users = [{"first_name": None, "last_name": "NoName", "full_name": ""}]
        restore_names(users)
        self.assertIsNone(users[0]["first_name"])

    def test_no_first_name_and_single_last_name(self):
        users = [{"first_name": None, "last_name": "Smith", "full_name": "Smith"}]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Smith")

    def test_multiple_users_with_empty_full_name(self):
        users = [
            {"first_name": None, "last_name": "Doe", "full_name": ""},
            {"first_name": None, "last_name": "Smith", "full_name": ""}
        ]
        restore_names(users)
        for user in users:
            self.assertIsNone(user["first_name"])

    def test_no_first_name_and_no_full_name(self):
        users = [{"first_name": None, "last_name": "NoName", "full_name": None}]
        restore_names(users)
        self.assertIsNone(users[0]["first_name"])


if __name__ == "__main__":
    unittest.main()