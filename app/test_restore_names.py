import pytest
from app.restore_names import restore_names

@pytest.mark.parametrize("users, expected", [
    (
        # input
        [
            {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}
        ],
        # output esperado
        [
            {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}
        ]
    ),
    (
            # input
            [
                {"first_name": "", "last_name": "Holy", "full_name": "Jack Holy"}
            ],
            # output esperado
            [
                {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}
            ]
    ),
    (
            # input
            [
                {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}
            ],
            # output esperado
            [
                {"first_name": "Jack", "last_name": "Holy", "full_name": "Jack Holy"}
            ]
    ),
])
def test_restore_names(users, expected) -> None:
    restore_names(users)
    assert users == expected


@pytest.mark.parametrize("bad_input",
                         [
                             3.5,
                             10,
                             [1],
                             {"word": 10}
                         ]
                         )
def test_restore_names_non_dict_raises(bad_input: object):
    with pytest.raises(AttributeError):
        restore_names(bad_input)