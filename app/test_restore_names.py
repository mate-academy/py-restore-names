import pytest
import copy
from typing import List

import app.restore_names


@pytest.mark.parametrize(
    "incomplete_users,complete_users",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }
            ],
            [
                {"first_name": "Jack",
                 "last_name": "Holy",
                 "full_name": "Jack Holy"
                 },
                {"first_name": "Mike",
                 "last_name": "Adams",
                 "full_name": "Mike Adams"
                 }
            ]
        )
    ]
)
def test_restore_names(
    incomplete_users: List[dict],
    complete_users: List[dict]
) -> None:
    working_list: List[dict] = copy.deepcopy(incomplete_users)
    print(f"\nlist pre: {working_list}")
    app.restore_names.restore_names(working_list)
    print(f"list post: {working_list}")
    assert (working_list == complete_users), \
        f"Failed with incomplete users: \n {incomplete_users}\n {working_list}"
