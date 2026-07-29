from app.restore_names import restore_names


# @pytest.mark.parametrize(
#     "first_name_before, first_name_after",
#     [
#         (
#             None,
#             "Jack"
#         ),
#         (
#             "",
#             "Mike"
#         )
#     ]
# )
# def test_correct_first_name(first_name_before, first_name_after):
#     user = [
#               {
#                 "first_name": first_name_before,
#                 "last_name": "Holy",
#                 "full_name": "Jack Holy",
#               }
#     ]
#     restore_names(user)
#     assert user[0]["first_name"] == first_name_after


def test_correct_first_name():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack" \
           and users[1]["first_name"] == "Mike"


def test_none_first_name():
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_no_first_name():
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        }
    ]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"
