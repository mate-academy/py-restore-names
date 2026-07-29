from unittest import TestCase

from app.restore_names import restore_names


class TestUser(TestCase):
    def setUp(self) -> None:
        self.users = [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]

    def test_first_name_present(self) -> None:
        restore_names(self.users)
        assert self.users == [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]

    def test_first_name_none(self) -> None:
        for user in self.users:
            user["first_name"] = None
        restore_names(self.users)
        assert self.users == [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]

    def test_first_name_key_absent(self) -> None:
        for user in self.users:
            del user["first_name"]
        restore_names(self.users)
        assert self.users == [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]
