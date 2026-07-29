import pytest
from app.restore_names import restore_names


class TestReturnFirstName:
    @pytest.mark.parametrize(
        "users,expected_result",
        [
            pytest.param(
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
                        "last_name": "Adams",
                        "full_name": "Mike Adams",
                        "first_name": "Mike"
                    },
                ],
                id="should return first name"
            )
        ]
    )
    def test_should_return_first_name(
            self,
            users: list,
            expected_result: list
    ) -> None:
        restore_names(users)
        assert users == expected_result
