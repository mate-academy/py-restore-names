import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "list_of_names, expected",
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
                }
            ]
        ),
        (
            [
                {
                    "first_name": "Clark",
                    "last_name": "Brown",
                    "full_name": "Clark Brown",
                },
                {
                    "last_name": "Smith",
                    "full_name": "Henry Smith",
                }
            ],
            [
                {
                    "first_name": "Clark",
                    "last_name": "Brown",
                    "full_name": "Clark Brown",
                },
                {
                    "first_name": "Henry",
                    "last_name": "Smith",
                    "full_name": "Henry Smith",
                }
            ]
        ),
        (
            [
                {
                    "first_name": None,
                    "last_name": "Uzumaki",
                    "full_name": "Naruto Uzumaki",
                },
                {
                    "last_name": "Uchiha",
                    "full_name": "Sasuke Uchiha",
                }
            ],
            [
                {
                    "first_name": "Naruto",
                    "last_name": "Uzumaki",
                    "full_name": "Naruto Uzumaki",
                },
                {
                    "first_name": "Sasuke",
                    "last_name": "Uchiha",
                    "full_name": "Sasuke Uchiha",
                }
            ]
        )
    ]
)
def test_restore_names(list_of_names: list, expected: list) -> None:
    restore_names(list_of_names)
    assert list_of_names == expected
