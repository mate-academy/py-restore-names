from unittest import TestCase

from app.restore_names import restore_names


class TestUsers(TestCase):
    def setUp(self) -> None:
        self.users = [
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

    def tearDown(self) -> None:
        del self.users

    def test_should_implement_first_name(self) -> None:
        restore_names(self.users)
        user_full_name = self.users[0]["full_name"].split()[0]
        assert (self.users[0]["first_name"] == user_full_name)
        user_full_name = self.users[1]["full_name"].split()[0]
        assert (self.users[1]["first_name"] == user_full_name)
