import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected",
    [
        pytest.param([
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
            id="if no 'first_name' or first_name' is None "
               "'first_name' should be added"),
        # pytest.param(
        #     [
        #     {
        #         "last_name": "Holy",
        #         "full_name": "Jack Holy",
        #       },
        #       {
        #         "last_name": "Adams",
        #         "full_name": "Mike Adams",
        #       },
        #     ],
        #     [
        #       {
        #         "first_name": "Jack",
        #         "last_name": "Holy",
        #         "full_name": "Jack Holy",
        #       },
        #       {
        #         "first_name": "Mike",
        #         "last_name": "Adams",
        #         "full_name": "Mike Adams",
        #       },
        #     ],
        #     id="'look' is not isogram"),
        # pytest.param(
        #     "Adam",
        #     False,
        #     id="'Adam' is not isogram"),
        # pytest.param(
        #     '',
        #     True,
        #     id="Empty string is True"),
    ]
)
def test_restore_names(users, expected):
    assert restore_names(users) == expected
