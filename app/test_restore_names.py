import pytest

from app.restore_names import restore_names


class TestRestoreNames:
    @pytest.mark.parametrize(
        "goal, res_goal",
        [
            pytest.param(
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy",
                    },
                ],
                [
                    {
                        'first_name': 'Jack',
                        'last_name': 'Holy',
                        'full_name': 'Jack Holy',
                    },
                ],
                id="first name isnone"
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
                        'last_name': 'Adams',
                        'full_name': 'Mike Adams',
                        'first_name': 'Mike'
                    }
                ],
                id="first name is missing"
            )
        ]
    )
    def test_correctly_first_name(
            self,
            goal,
            res_goal
    ):
        restore_names(goal)

        assert goal == res_goal
