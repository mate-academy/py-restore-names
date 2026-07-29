import pytest
from app.restore_names import restore_names


class TestCheckName:
    @pytest.mark.parametrize(
        "initial, expected",
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
                id="Check first name when it's None"
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
                id="Check first name when it's not exist"
            ),
        ]
    )
    def test_fist_name(
            self,
            initial,
            expected
    ):
        restore_names(initial)
        assert initial == expected
