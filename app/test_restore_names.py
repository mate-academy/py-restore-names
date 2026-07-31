import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize("users, expected", [
        pytest.param(
            [
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
            id="updates none first name",
        ),
        pytest.param(
            [
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
                }
            ],
            id="adds missing first name key",
        ),
        pytest.param(
            [
                {
                    "first_name": "",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            id="does not update empty string first name",
        ),
        pytest.param(
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                }
            ],
            id="leaves existing valid first name unchanged",
        ),
        pytest.param(
            [],
            [],
            id="handles empty list",
        ),
    ])
    def test_restore_names_adds_first_name(self, users, expected) -> None:
        restore_names(users)
        assert users == expected