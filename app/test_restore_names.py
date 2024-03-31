import pytest
from app.restore_names import restore_names


# write your tests here
class TestRestoreNames:

    @pytest.fixture()
    def users(self) -> list:
        return [
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

    def test_should_restore_names(self, users: list) -> None:
        restore_names(users)
        assert users == [
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

    def test_should_return_nothing(self, users: list) -> None:
        assert restore_names(users) is None
