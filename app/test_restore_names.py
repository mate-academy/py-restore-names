from app.restore_names import restore_names


def test_user_with_no_name() -> None:
    user = [{"last_name": "Holy", "full_name": "Jack Holy"}]
    restore_names(user)
    assert user[0].get("first_name") == "Jack"


def test_user_with_name_none() -> None:
    user = [{"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"}]
    restore_names(user)
    assert user[0].get("first_name") == "Jack"
