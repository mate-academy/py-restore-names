from unittest import TestCase

from app.restore_names import restore_names


class TestName(TestCase):

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

    def test_restore_expected(self) -> None:
        restore_names(self.users)

        assert self.users == [
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
