import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_dict,expected_dict",
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
                },
            ],
            id="should restore correctly"
        ),
        pytest.param(
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
            id="should not change when first_name is not None"
        ),
        pytest.param(
            [
                {
                    "last_name": "Adams",
                    "full_name": "Mike-Kostia Adams",
                }
            ],
            [
                {
                    "first_name": "Mike-Kostia",
                    "last_name": "Adams",
                    "full_name": "Mike-Kostia Adams",
                },
            ],
            id="should work correctly if user has double name"
        ),

    ]
)
def test_restore_names(
        input_dict: list[dict],
        expected_dict: list[dict]
) -> None:
    restore_names(input_dict)
    assert input_dict == expected_dict
