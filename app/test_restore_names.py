import unittest
from app.restore_names import restore_names

class UserTestCase(unittest.TestCase):
    def setUp(self):
        self.user_with_none = {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
        self.user_without_first_name = {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
        self.user_with_first_name = {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith"
        }

    def test_restore_from_none(self):
        users = [self.user_with_none.copy()]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Jack")

    def test_restore_from_missing(self):
        users = [self.user_without_first_name.copy()]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Mike")

    def test_dont_override_existing_first_name(self):
        users = [self.user_with_first_name.copy()]
        restore_names(users)
        self.assertEqual(users[0]["first_name"], "Anna")

if __name__ == "__main__":
    unittest.main()
