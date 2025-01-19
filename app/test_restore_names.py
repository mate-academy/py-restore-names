import pytest
from app.restore_names import restore_names


class TestRestoreNamesClass:
    @pytest.fixture()
    def users_data_template(self) -> list:
        users = [
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
        return users

    def test_users_first_name_is_numeric(self,
                                         users_data_template: list
                                         ) -> None:
        users_data_template[0]["first_name"] = 1
        restore_names(users_data_template)
        assert users_data_template[0]["first_name"] == 1

    def test_users_first_name_is_bool(self, users_data_template: list) -> None:
        users_data_template[0]["first_name"] = False
        restore_names(users_data_template)
        assert users_data_template[0]["first_name"] is False

    def test_users_first_name_is_none(self, users_data_template: list) -> None:
        users_data_template[0]["first_name"] = None
        restore_names(users_data_template)
        assert users_data_template[0]["first_name"] == "Jack"

    def test_users_first_name_is_empty_string(self,
                                              users_data_template: list
                                              ) -> None:
        users_data_template[0]["first_name"] = ""
        restore_names(users_data_template)
        assert users_data_template[0]["first_name"] == ""
