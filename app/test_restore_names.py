import pytest
from app.restore_names import restore_names


class TestRestoreNames:

    @pytest.fixture
    def user(self) -> dict:
        return {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }

    @pytest.mark.parametrize(
        "first_name, expected",
        [
            pytest.param(None, "Jack", id="first_name is None"),
            pytest.param("Jack", "Jack", id="first_name already exists"),
        ]
    )
    def test_restore_names(
            self,
            user: dict,
            first_name: str,
            expected: str
    ) -> None:
        user["first_name"] = first_name
        users = [user]
        restore_names(users)
        assert users[0]["first_name"] == expected

    def test_restore_names_without_first_name(self, user: dict) -> None:
        del user["first_name"]
        users = [user]
        restore_names(users)
        assert users[0]["first_name"] == "Jack"
