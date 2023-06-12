import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.fixture(scope="module")
    def users_template(self) -> list:
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

    def test_should_change_first_name_from_none_to_first_name(
            self,
            users_template: list[dict]
    ) -> None:
        restore_names(users_template)
        assert (
            users_template[0] == {
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }
        )

    def test_should_add_first_name_key_with_name(
            self,
            users_template: list[dict]
    ) -> None:
        assert (
            users_template[1] == {
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }
        )
