import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.fixture()
    def broken_users_template(self) -> list[dict]:
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

    @pytest.fixture()
    def repaired_users_template(self) -> list[dict]:
        return [
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

    def test_restore_names(self,
                           broken_users_template: list[dict],
                           repaired_users_template: list[dict]) -> None:
        restore_names(broken_users_template)
        assert broken_users_template == repaired_users_template
