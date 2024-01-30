import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "input_dict, expected_output",
    [
        (
            [{"first_name": None,
              "last_name": "Dobrovinskii",
              "full_name": "Serhii Dobrovinskii"},
             {"last_name": "Kluch",
              "full_name": "Ivan Kluch"}],
            [{"first_name": "Serhii",
              "last_name": "Dobrovinskii",
              "full_name": "Serhii Dobrovinskii"},
             {"first_name": "Ivan",
              "last_name": "Kluch",
              "full_name": "Ivan Kluch"}]
        )
    ]
)
def test_restore_names(input_dict: list, expected_output: dict) -> None:
    restore_names(input_dict)
    assert input_dict == expected_output
