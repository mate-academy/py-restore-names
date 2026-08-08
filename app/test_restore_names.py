import pytest
from app import restore_names as restore_names_module


# write your tests here
@pytest.mark.parametrize(
    "names, expected",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Doe",
                    "full_name": "John Doe",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                }
            ]
        ),
        pytest.param(
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                }
            ]
        ),
        pytest.param(
            [
                {
                    "last_name": "Doe",
                    "full_name": "John Doe",
                }
            ],
            [
                {
                    "first_name": "John",
                    "last_name": "Doe",
                    "full_name": "John Doe",
                }
            ]
        ),
    ]
)
def test_restore_names(
    names: list[dict[str, str]],
    expected: list[dict[str, str]]
) -> None:
    restore_names_module.restore_names(names)
    assert names == expected
