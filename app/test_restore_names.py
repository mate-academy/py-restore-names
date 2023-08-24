from unittest import TestCase

from app.restore_names import restore_names


class TestRestoreNames(TestCase):
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
            {
                "first_name": "John",
                "last_name": "Adams",
                "full_name": "John Adams",
            },
        ]

    def test_change_first_name(self) -> None:
        restore_names(self.users)
        assert self.users[0]["first_name"] == "Jack"

    def test_add_first_name(self) -> None:
        restore_names(self.users)
        assert self.users[1]["first_name"] == "Mike"

    def test_nothing_changed_if_has_name(self) -> None:
        name_before = self.users[2]["first_name"]
        restore_names(self.users)
        assert name_before == self.users[2]["first_name"]
