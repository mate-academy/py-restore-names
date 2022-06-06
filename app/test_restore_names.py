import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users, expected",
        [
            pytest.param([
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
                [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                }
            ],
                id="if 'first_name' is None "
                   "'first_name' should be added"),
            pytest.param([
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
                [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
                id="if no 'first_name'"
                   "'first_name' should be added")
        ]
    )
    def test_restore_names(self, users, expected):
        assert restore_names(users) == expected
