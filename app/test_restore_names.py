from unittest import TestCase
from app.restore_names import restore_names


class TestRestoreName(TestCase):

    def setUp(self) -> None:
        self.incorrect_users = [
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
        self.correct_users = [
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

    def test_restore_first_name_is_none(self) -> None:
        restore_names(self.incorrect_users)
        assert self.incorrect_users == self.correct_users
