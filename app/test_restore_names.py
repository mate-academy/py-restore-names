import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "failed_info, expected",
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
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ]
        ),
        (
            [
                {
                    "first_name": "Dmytro",
                    "last_name": "Petrykiv",
                    "full_name": "Dmytro Petrykiv",
                },
                {
                    "first_name": "Bib",
                    "last_name": "Taras",
                    "full_name": "Biber Tarik",
                },
            ],
            [
                {
                    "first_name": "Dmytro",
                    "last_name": "Petrykiv",
                    "full_name": "Dmytro Petrykiv",
                },
                {
                    "first_name": "Bib",
                    "last_name": "Taras",
                    "full_name": "Biber Tarik",
                },
            ]
        ),
    ]
)
def test_restore_name(failed_info: list, expected: list) -> None:
    restore_names(failed_info)
    assert failed_info == expected
