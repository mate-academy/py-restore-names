from app.restore_names import restore_names


def test_restore_names_if_first_name_is_none() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_restore_names_if_not_first_name() -> None:
    users = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy",
        }]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"
