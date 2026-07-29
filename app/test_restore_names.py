from app.restore_names import restore_names


def test_users_whose_first_name_equal_to_none() -> None:
    users = [{
        "first_name": None, "last_name": "Jones", "full_name": "David Jones"}]
    restore_names(users)
    assert users[0]["first_name"] == "David"


def test_users_whose_first_name_is_missing() -> None:
    users = [{
        "last_name": "Williams", "full_name": "Max Williams"}]
    restore_names(users)
    assert users[0]["first_name"] == "Max"
