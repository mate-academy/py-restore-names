import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_dict,output_dict",
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
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            id="should return correctly result list"
        )
    ]
)
def test_should_return_correctly_result_list(
    input_dict: list,
    output_dict: list
) -> None:
    restore_names(input_dict)
    assert input_dict == output_dict
