import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_list,out_list",
    [
        (
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }]
        ),
        (
            [{
                "last_name": "Lite",
                "full_name": "Eva Lite",
            }],
            [{
                "first_name": "Eva",
                "last_name": "Lite",
                "full_name": "Eva Lite",
            }]
        )
    ]
)
def test_restore_names(input_list: list, out_list):
    restore_names(input_list)
    assert input_list == out_list
