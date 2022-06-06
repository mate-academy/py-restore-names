import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "broken_user, fixed_user",
        [
            (
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
                ]
            ),
            (
                [
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ],
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ]
            ),
            (
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ],
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    }
                ]
            )
        ]
    )
    def test_names_are_restored_correctly(self, broken_user, fixed_user):
        restore_names(broken_user)
        assert fixed_user == broken_user
