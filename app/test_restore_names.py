import pytest
from app.restore_names import restore_names


class TestRestoreNamesApp:
    @pytest.mark.parametrize(
        "initial_database,expected_database",
        [
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
                id="First name is None value"
            ),
            pytest.param(
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
                ],
                id="First name is missing"
            ),
            pytest.param(
                [
                    {
                        "first_name": "Jack",
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
                id="When every fields are"
            ),
        ]
    )
    def test_correct(
            self,
            initial_database: str,
            expected_database: dict
    ) -> None:
        assert restore_names(initial_database) == expected_database
