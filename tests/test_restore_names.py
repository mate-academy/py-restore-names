from app.restore_names import restore_names


def test_function_should_return_none():
    assert restore_names([]) is None


def test_function_should_set_correct_first_name_if_it_none_or_missing():
    users = [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"last_name": "Adams",
              "full_name": "Mike Adams"}]
    restore_names(users)
    correct_users = [{"first_name": "Jack",
                      "last_name": "Holy",
                      "full_name": "Jack Holy"},
                     {"first_name": "Mike",
                      "last_name": "Adams",
                      "full_name": "Mike Adams"}]
    assert users == correct_users


def test_function_should_not_change_list_if_all_is_right():
    users = [{"first_name": "Jack",
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"first_name": "Mike",
              "last_name": "Adams",
              "full_name": "Mike Adams"}]
    correct_users = [{"first_name": "Jack",
                      "last_name": "Holy",
                      "full_name": "Jack Holy"},
                     {"first_name": "Mike",
                      "last_name": "Adams",
                      "full_name": "Mike Adams"}]
    restore_names(users)
    assert users == correct_users
