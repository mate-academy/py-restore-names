import pytest
from app.restore_names import restore_names


class TestRestoreNamesClass:
    @pytest.mark.parametrize(
        "user_to_restore, goal",
        [
            pytest.param(
                [
                    {
                        "first_name": "Eric",
                        "last_name": "Cantona",
                        "full_name": "Eric Cantona",
                    }
                ],
                [
                    {
                        "first_name": "Eric",
                        "last_name": "Cantona",
                        "full_name": "Eric Cantona",
                    }
                ],
                id="nothing to change"
            ),
            pytest.param(
                [
                    {
                        "last_name": "Zidane",
                        "full_name": "Zinedin Zidane",
                    }
                ],
                [
                    {
                        "first_name": "Zinedin",
                        "last_name": "Zidane",
                        "full_name": "Zinedin Zidane",
                    }
                ],
                id="should add key 'first_name' to user with value of name"
            ),
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Carlos",
                        "full_name": "Roberto Carlos",
                    }
                ],
                [
                    {
                        "first_name": "Roberto",
                        "last_name": "Carlos",
                        "full_name": "Roberto Carlos",
                    }
                ],
                id="should add first name until None"
            )
        ]
    )
    def test_restore_names_correctly(
            self,
            user_to_restore,
            goal
    ):
        restore_names(user_to_restore)
        assert user_to_restore == goal
