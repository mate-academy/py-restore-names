from app.restore_names import restore_names


def test_restore_names_with_name_none() -> None:
    test_user = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
    restore_names(test_user)
    assert test_user[0].get("first_name") == "Jack"


def test_restore_names_with_no_name() -> None:
    test_user = [{
        "last_name": "Holy",
        "full_name": "Jack Holy"
    }]
    restore_names(test_user)
    assert test_user[0].get("first_name") == "Jack"
