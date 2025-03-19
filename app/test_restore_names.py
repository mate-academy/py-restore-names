import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize("users, restored_users", [
        ([{"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
          {"last_name": "Adams", "full_name": "Mike Adams"}],
         [{"first_name": "Jack",
           "last_name": "Holy",
           "full_name": "Jack Holy"},
          {"last_name": "Adams",
           "full_name": "Mike Adams",
           "first_name": "Mike"}])])
    def test_restore_names(self, users: list, restored_users: list) -> None:

        restore_names(users)

        assert users == restored_users
