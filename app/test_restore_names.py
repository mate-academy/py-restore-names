from typing import Any, List

import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("dictionary, expected_result", [
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
        ],
    )
])
def test_restore_names(dictionary: List[dict],
                       expected_result: List[dict]) -> None:
    restore_names(dictionary)
    assert dictionary == expected_result


@pytest.mark.parametrize("invalid_input", [
    "10",
    [10],
    None,
])
def test_get_type_error(invalid_input: Any) -> None:
    with pytest.raises(TypeError):
        restore_names(invalid_input)
