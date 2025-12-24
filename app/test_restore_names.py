import pytest
from app.restore_names import restore_names


class TestRestore:
    @pytest.mark.parametrize(
        "income, result",
        [
            (
                [{"last_name": "Holy", "full_name": "Jack Holy"}],
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }
                ],
            ),
            (
                [
                    {
                        "first_name": None,
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }
                ],
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }
                ],
            ),
            (
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }
                ],
                [
                    {
                        "first_name": "Jack",
                        "last_name": "Holy",
                        "full_name": "Jack Holy"
                    }
                ],
            ),
            (
                [
                    {
                        "first_name": None,
                        "last_name": "Adams",
                        "full_name": "Mike Adams"
                    }
                ],
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams"
                    }
                ],
            ),
            (
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams"
                    }
                ],
                [
                    {
                        "first_name": "Mike",
                        "last_name": "Adams",
                        "full_name": "Mike Adams"
                    }
                ],
            ),
        ]
    )
    def test_restore(self, income: list[dict], result: list[dict]) -> None:
        restore_names(income)
        assert income == result
