import unittest


from app.restore_names import restore_names


class TestRestoreNames(unittest.TestCase):
    def test_restore_when_first_name_is_none(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
        ]
        restore_names(users)
        expected = [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy"
            },
            {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams"
            },
        ]
        self.assertEqual(users, expected)

    def test_no_change_when_first_name_exists(self) -> None:
        users = [
            {
                "first_name": "Anna",
                "last_name": "Smith",
                "full_name": "Anna Smith"
            },
        ]
        expected = [
            {
                "first_name": "Anna",
                "last_name": "Smith",
                "full_name": "Anna Smith"
            },
        ]
        restore_names(users)
        self.assertEqual(users, expected)

    def test_partial_full_name(self) -> None:
        users = [
            {
                "first_name": None,
                "last_name": "Doe",
                "full_name": "John"
            },
        ]
        expected = [
            {
                "first_name": "John",
                "last_name": "Doe",
                "full_name": "John"
            },
        ]
        restore_names(users)
        self.assertEqual(users, expected)
