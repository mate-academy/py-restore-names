from unittest import TestCase
from app.restore_names import restore_names


class TestRestoreNameFunc(TestCase):
    def setUp(self) -> None:
        self.user = [
            {
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]

    def tearDown(self) -> None:
        delattr(self, "user")

    def test_should_set_first_name_value_when_first_name_is_none(self) -> None:
        restore_names(self.user)
        assert self.user == {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }

    def test_should_set_first_name_key_and_value_when_first_name_not_exist(
            self
    ) -> None:
        del self.user[0]["first_name"]
        restore_names(self.user)
        assert self.user == {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }
