import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize("initial_users, expected_first_name",
                         [
                             pytest.param(
                                 [{
                                     "first_name": None,
                                     "last_name": "Holy",
                                     "full_name": "Jack Holy",
                                 }],
                                 "Jack",
                                 id="add first name when none provided"),
                             pytest.param(
                                 [{
                                     "last_name": "Adams",
                                     "full_name": "Mike Adams",
                                 }],
                                 "Mike",
                                 id="add first name when completely missing"),
                             pytest.param(
                                 [{
                                     "first_name": "Sam",
                                     "last_name": "Smith",
                                     "full_name": "Sam Smith",
                                 }],
                                 "Sam",
                                 id="no changes when first name provided"),
                         ])
def test_modify_first_name_correctly(initial_users, expected_first_name):
    restore_names(initial_users)
    assert initial_users[0]["first_name"] == expected_first_name
