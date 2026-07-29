import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("users_template, expected_name",
                         [([{
                             "first_name": None,
                             "last_name": "Holy",
                             "full_name": "Jack Holy",
                         }, {
                             "first_name": "Mike",
                             "last_name": "Adams",
                             "full_name": "Mike Adams",
                         }, ], ["Jack", "Mike"]),
                             ([{
                                 "last_name": "Holy",
                                 "full_name": "Jack Holy",
                             }, {
                                 "first_name": "Mike",
                                 "last_name": "Adams",
                                 "full_name": "Mike Adams",
                             }, ], ["Jack", "Mike"]),
                         ])
def test_restore_names(users_template: list, expected_name: list) -> None:
    restore_names(users_template)

    for i in range(len(users_template)):
        assert users_template[i]["first_name"] == expected_name[i]
