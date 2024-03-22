from app.restore_names import restore_names


def test_basic_functionality() -> None:
    users = [
        {"first_name": None, "last_name": "Ko", "full_name": "Ivan Ko"},
        {"last_name": "Li", "full_name": "Anna Li"}
    ]
    expected = [
        {"first_name": "Ivan", "last_name": "Ko", "full_name": "Ivan Ko"},
        {"first_name": "Anna", "last_name": "Li", "full_name": "Anna Li"}
    ]
    restore_names(users)
    assert users == expected


def test_empty_list() -> None:
    users = []
    restore_names(users)
    assert users == []


def test_unmodified_first_name() -> None:
    expected = [
        {
            "first_name": "Ola",
            "last_name": "Vu",
            "full_name": "Ola Vu"
        }
    ]
    users = [
        {"first_name": "Ola", "last_name": "Vu", "full_name": "Ola Vu"}
    ]
    restore_names(users)
    assert users == expected


def test_no_last_name() -> None:
    users = [{"first_name": None, "full_name": "Leo"}]
    expected = [{"first_name": "Leo", "full_name": "Leo"}]
    restore_names(users)
    assert users == expected


def test_single_name_full_name() -> None:
    users = [{"first_name": None, "last_name": "Sy", "full_name": "Max"}]
    expected = [{"first_name": "Max", "last_name": "Sy", "full_name": "Max"}]
    restore_names(users)
    assert users == expected
