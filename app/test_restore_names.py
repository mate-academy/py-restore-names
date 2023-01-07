import pytest
from app.restore_names import restore_names


class TestRestoreName:

    @pytest.fixture()
    def users_template(self) -> list:
        return [
            {
                "last_name": "Holy",
                "full_name": "Jack Holy",
            },
        ]

    def test_restore_without_name(self, users_template: list) -> None:
        restore_names(users_template)
        assert users_template == [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]

    def test_restore_with_name_equal_to_none(
            self,
            users_template: list
    ) -> None:
        users_template[0]["first_name"] = None
        restore_names(users_template)
        assert users_template == [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]

    def test_restore_with_no_problems(self, users_template: list) -> None:
        users_template[0]["first_name"] = "Jack"
        restore_names(users_template)
        assert users_template == [
            {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        ]
