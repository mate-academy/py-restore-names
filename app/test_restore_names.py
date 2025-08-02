from app.restore_names import restore_names


def test_should_handle_absence_off_first_name() -> None:
    users = [
        {
            "last_name": "Adams",
            "full_name": "Anna Adams",
        }
    ]
    restore_names(users)
    expected_list = [
        {
            "first_name": "Anna",
            "last_name": "Adams",
            "full_name": "Anna Adams",
        }
    ]
    assert users == expected_list


def test_should_handle_none_first_name() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Berry",
            "full_name": "Holly Berry",
        }
    ]
    restore_names(users)
    expected_list = [
        {
            "first_name": "Holly",
            "last_name": "Berry",
            "full_name": "Holly Berry",
        }
    ]
    assert users == expected_list


def test_should_handle_multiple_users() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Lesh",
            "full_name": "Dash Lesh",
        },
        {
            "last_name": "Tkal",
            "full_name": "Illya Tkal",
        }
    ]
    restore_names(users)
    expected_list = [
        {
            "first_name": "Dash",
            "last_name": "Lesh",
            "full_name": "Dash Lesh",
        },
        {
            "first_name": "Illya",
            "last_name": "Tkal",
            "full_name": "Illya Tkal",
        }
    ]
    assert users == expected_list


def test_should_handle_empty_list() -> None:
    users = []
    restore_names(users)
    expected_list = []
    assert users == expected_list
