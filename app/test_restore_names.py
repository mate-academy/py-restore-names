import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "user, expected_output", [
            ({"full_name": "John Doe", "first_name": None},
             {"full_name": "John Doe", "first_name": "John"}),
            ({"full_name": "Alice Smith", "last_name": "Smith"},
             {"full_name": "Alice Smith", "last_name": "Smith",
              "first_name": "Alice"}),
            ({"full_name": "Bob Johnson"},
             {"full_name": "Bob Johnson", "first_name": "Bob"}),
        ])
    def test_restore_names(
            self,
            user: dict,
            expected_output: dict,
    ) -> None:
        user = [user]
        restore_names(user)
        assert user == [expected_output]
