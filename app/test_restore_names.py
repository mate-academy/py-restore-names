import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_lst,output_lst",
    [
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
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                    "first_name": "Mike",
                },
            ]
        )
    ]
)
def test_restore_names(input_lst: list, output_lst: list) -> None:
    restore_names(input_lst)
    print(input_lst)
    assert input_lst == output_lst
