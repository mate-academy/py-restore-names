import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "given_dict, expected_dict",
    [
        ([{
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }], [{
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }]),
        ([{
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }], [{
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }])

    ]
)
def test_restore_names(
        given_dict: list[dict],
        expected_dict: list[dict]
) -> None:
    restore_names(given_dict)
    assert given_dict == expected_dict
