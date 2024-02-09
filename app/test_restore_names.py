import pytest
from app.restore_names import restore_names


class TestRestoreNames():
    @pytest.fixture()
    def user_template(self) -> list[dict]:
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

    def test_restore_names(self, user_template: list[dict]) -> None:
        restore_names(user_template)
        assert user_template == [
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
