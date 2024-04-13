from app.restore_names import restore_names

asserted_list = [{
    "first_name": "Jack",
    "last_name": "Holy",
    "full_name": "Jack Holy",
}]


def test_func_should_restore_none() -> None:
    test_dict = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]
    restore_names(test_dict)
    assert test_dict == asserted_list


def test_func_should_restore_missing_line() -> None:
    test_dict = [{
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]
    restore_names(test_dict)
    assert test_dict == asserted_list
