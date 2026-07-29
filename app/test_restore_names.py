import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "initial_list, adding_key, expected_value",
    [
        (
            pytest.param(
                [{"full_name": "Sherlock Holmes"}],
                "first_name",
                "Sherlock",
                id="missing first name"
            )
        ),
        (
            pytest.param(
                [{"first_name": None,
                  "full_name": "Sherlock Holmes"}],
                "first_name",
                "Sherlock",
                id="none first name"
            )
        ),
        (
            pytest.param(
                [{"first_name": "Sherlok",
                  "full_name": "Sherlock Holmes"}],
                "first_name",
                "Sherlok",
                id="existing first name"
            )
        )
    ]
)
def test_restore_names(
        initial_list: list[dict],
        adding_key: str,
        expected_value: str) -> None:
    restore_names(initial_list)
    assert initial_list[0][adding_key] == expected_value
