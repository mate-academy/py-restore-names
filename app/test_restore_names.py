import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_info, correct_users_info",
    [
        # test_first_name_none_single_user
        pytest.param(
            [{
                "first_name": None,
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            [{
                "first_name": "Jack",
                "last_name": "Holy",
                "full_name": "Jack Holy",
            }],
            id="first name none single user",
        ),
        # test_first_name_not_found_single_user
        pytest.param(
            [{
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            [{
                "first_name": "Mike",
                "last_name": "Adams",
                "full_name": "Mike Adams",
            }],
            id="first name not in single use",
        ),
        # test_few_users
        pytest.param(
            [{
                "last_name": "Smith",
                "full_name": "John Smith", },
                {
                "first_name": None,
                "last_name": "Black",
                "full_name": "Lily Black",
            }],
            [{
                "first_name": "John",
                "last_name": "Smith",
                "full_name": "John Smith", },
                {
                "first_name": "Lily",
                "last_name": "Black",
                "full_name": "Lily Black",
            }],
            id="few users",
        ),
        # test_users_with_first_name
        pytest.param(
            [{
                "last_name": "Smith",
                "full_name": "John Smith", },
                {
                    "first_name": None,
                    "last_name": "Black",
                    "full_name": "Lily Black",
            }],
            [{
                "first_name": "John",
                "last_name": "Smith",
                "full_name": "John Smith", },
                {
                    "first_name": "Lily",
                    "last_name": "Black",
                    "full_name": "Lily Black",
            }],
            id="users with first name",
        ),
    ]
)
def test_(users_info: list[dict], correct_users_info: list[dict]) -> None:
    users = users_info
    restore_names(users)
    assert users == correct_users_info

#
# def test_first_name_none_single_user() -> None:
#     user = [
#         {
#             "first_name": None,
#             "last_name": "Holy",
#             "full_name": "Jack Holy",
#         }
#     ]
#
#     restore_names(user)
#     assert user == [
#         {
#             "first_name": "Jack",
#             "last_name": "Holy",
#             "full_name": "Jack Holy",
#         }
#     ]
#
#
# def test_first_name_not_found_single_user() -> None:
#     user = [
#         {
#             "last_name": "Adams",
#             "full_name": "Mike Adams",
#         }
#     ]
#
#     restore_names(user)
#     assert user == [
#         {
#             "first_name": "Mike",
#             "last_name": "Adams",
#             "full_name": "Mike Adams",
#         }
#     ]

#
# def test_few_users() -> None:
#     users = [
#         {
#             "last_name": "Smith",
#             "full_name": "John Smith",
#         },
#         {
#             "first_name": None,
#             "last_name": "Black",
#             "full_name": "Lily Black",
#         },
#     ]
#
#     restore_names(users)
#     assert users == [
#         {
#             "first_name": "John",
#             "last_name": "Smith",
#             "full_name": "John Smith",
#         },
#         {
#             "first_name": "Lily",
#             "last_name": "Black",
#             "full_name": "Lily Black",
#         },
#     ]
#
#
# def test_users_with_first_name() -> None:
#     users = [
#         {
#             "first_name": "Jack",
#             "last_name": "Holy",
#             "full_name": "Jack Holy",
#         },
#         {
#             "first_name": "Mike",
#             "last_name": "Adams",
#             "full_name": "Mike Adams",
#         },
#     ]
#
#     restore_names(users)
#     assert users == [
#         {
#             "first_name": "Jack",
#             "last_name": "Holy",
#             "full_name": "Jack Holy",
#         },
#         {
#             "first_name": "Mike",
#             "last_name": "Adams",
#             "full_name": "Mike Adams",
#         },
#     ]
