from typing import Any

import pytest
from app.restore_names import restore_names


class TestRestoreName:

    @pytest.mark.parametrize(
        "input_dict, result",
        [
            (
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
                        }
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
                        }
                    ],
                    id="test restore first name"
                )
            )
        ]
    )
    def test_func_return_correct_db(
            self,
            input_dict: list[dict],
            result: list[dict]
    ) -> None:
        restore_names(input_dict)
        assert input_dict == result

    @pytest.mark.parametrize(
        "input_dict, error",
        [
            (
                pytest.param(
                    [
                        {
                            "first_name": None,
                            "last_name": "Holy",
                            "full_name": "Jack Holy",
                        },
                        {
                            "last_name": "Adams",
                        }
                    ],
                    KeyError,
                    id="test without full name"
                )
            )
        ]
    )
    def test_raise_error_from_restore(
            self,
            input_dict: list[dict],
            error: Any
    ) -> None:
        with pytest.raises(error):
            restore_names(input_dict)
