import unittest
from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):

    def test_restore_names_with_missing_first_name(self) -> None:
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
        self.assertEqual(users, expected_users)

    def test_restore_names_with_existing_first_name(self) -> None:
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
        restore_names(users)
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
        self.assertEqual(users, expected_users)

    def test_restore_names_with_partial_missing_first_name(self) -> None:
        users = [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "first_name": None,
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
        restore_names(users)
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
        self.assertEqual(users, expected_users)

    def test_restore_names_with_no_first_name_and_no_full_name(self) -> None:
        users = [
            {
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams",
            },
        ]
        restore_names(users)
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
        self.assertEqual(users, expected_users)


if __name__ == "__main__":
    unittest.main()
