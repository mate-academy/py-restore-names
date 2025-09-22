from app.restore_names import restore_names


def test_restore_names_without_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": None,
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == [
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


def test_restore_names_without_last_name() -> None:
    users = [
        {
            "first_name": "Jack",
            "last_name": None,
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": None,
            "full_name": "Mike Adams",
        }
    ]
    restore_names(users)
    assert users == [
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


# def test_restore_without_full_name() -> None:
#     users = [
#         {
#             "first_name": "Jack",
#             "last_name": "Holy",
#             "full_name": None,
#         },
#         {
#             "first_name": "Mike",
#             "last_name": "Adams",
#             "full_name": None,
#         }
#     ]
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
#         }
#     ]


def test_restore_names_with_anything() -> None:
    users = [
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
    restore_names(users)
    assert users == [
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
