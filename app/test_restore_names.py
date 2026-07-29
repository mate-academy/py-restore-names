import pytest
from app.restore_names import restore_names

from copy import deepcopy

data_for_test = [
    ([{"first_name": None,
       "last_name": "Holy",
       "full_name": "Jack Holy", }],
     [{"first_name": "Jack",
       "last_name": "Holy",
       "full_name": "Jack Holy", }])
    ,
    ([{"last_name": "Adams",
       "full_name": "Mike Adams", }],
     [{"first_name": "Mike",
       "last_name": "Adams",
       "full_name": "Mike Adams", }])
]


def gen_keys(dataset: list) -> str:
    users, expected = dataset
    if "first_name" in users:
        return (f"user name was {users[0]['first_name']}, "
                f"user name is {expected[0]['first_name']}")
    return (f"we didn't have user name, "
            f"user name is {expected[0]['first_name']}")


@pytest.mark.parametrize("dataset",
                         data_for_test,
                         ids=gen_keys)
def test_restore_names(dataset: list) -> None:
    users, expected = dataset
    users_harcopy = deepcopy(users)
    restore_names(users_harcopy)
    assert users_harcopy == expected
