import pytest
from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "users, expected_users",
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
            )
        ]
    )
    def test_restore_names(self, users, expected_users):
        function_not_return = restore_names(users)

        assert function_not_return is None, (
            "Function shouldn't return anything"
        )
        assert users == expected_users, (
            f"Function 'restore_name' should update 'users' correctly! "
            f"When 'users' equal {users}"
        )

    def test_raising_error_correctly(self):
        users = [{}, {}]

        with pytest.raises(KeyError):
            restore_names(users)
