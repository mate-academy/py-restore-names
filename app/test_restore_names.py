import pytest
from app.restore_names import restore_names
from typing import List


@pytest.mark.parametrize("initial_user,result_user",
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
                                     {
                                         "first_name": "Jacek",
                                         "last_name": "Holewski",
                                         "full_name": "Jacek Holewski",
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
                                     },
                                     {
                                         "first_name": "Jacek",
                                         "last_name": "Holewski",
                                         "full_name": "Jacek Holewski",
                                     }
                                 ]
                             )
                         ]
                         )
def test_restore_names(
        initial_user: List[dict],
        result_user: List[dict]
) -> None:
    restore_names(initial_user)
    assert initial_user == result_user

# @pytest.fixture()
# def initial_user() -> List[dict]:
#     return [
#         {
#             "first_name": None,
#             "last_name": "Holy",
#             "full_name": "Jack Holy",
#         },
#         {
#             "last_name": "Adams",
#             "full_name": "Mike Adams",
#         },
#         {
#             "first_name": "Jacek",
#             "last_name": "Holewski",
#             "full_name": "Jacek Holewski",
#         }
#     ]
#
#
# def test_restore_names(initial_user: List[dict]) -> None:
#     restore_names(initial_user)
#     assert initial_user[0]["first_name"] == "Jack"
#     assert initial_user[1]["first_name"] == "Mike"
#     assert initial_user[2]["first_name"] == "Jacek"
