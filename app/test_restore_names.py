import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_dict, expected_dict",
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
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            id="test_restoring_if_first_name_is_None"
        ),
        pytest.param(
            [
                {
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
            ],
            id="test_restoring_if_no_first_name"
        )
    ]
)
def test_restore_names(
        input_dict: list[dict],
        expected_dict: list[dict]
) -> None:
    restore_names(input_dict)
    assert input_dict == expected_dict
