import pytest
from app.restore_names import restore_names


class TestAddValueClass:
    @pytest.mark.parametrize(
        "initial_classes,expected_classes",
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
                ],
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
                ],
            ),
        ],
    )
    def test_check_full_user_name(self,
                                  initial_classes: list,
                                  expected_classes: list) -> None:
        assert restore_names(initial_classes) \
               == restore_names(expected_classes)
