import pytest
from app.restore_names import restore_names


class TestRestoreNames:

    @pytest.mark.parametrize(
        "users_lost_values, users_restore",
        [
            (
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    },
                    {
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                    },
                ],
                [
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
            ),
            (
                [
                    {
                        "first_name": None,
                        "last_name": "Blake",
                        "full_name": "Marry Blake",
                    },
                    {
                        "last_name": "Weiss",
                        "full_name": "John Weiss",
                    },
                ],
                [
                    {
                        "first_name": "Marry",
                        "last_name": "Blake",
                        "full_name": "Marry Blake",
                    },
                    {
                        "first_name": "John",
                        "last_name": "Weiss",
                        "full_name": "John Weiss",
                    },
                ]
            ),

        ]

    )
    def test_right_restore_names(self,
                                 users_lost_values: list,
                                 users_restore: list) -> None:
        users = users_lost_values
        restore_names(users)
        assert users == users_restore
