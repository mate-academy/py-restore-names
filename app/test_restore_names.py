from app.restore_names import restore_names


def test_should_restore_name_if_key_first_name_does_not_exist() -> None:
    user = {"last_name": "Belly", "full_name": "Chris Belly"}
    restore_names([user])
    assert user["first_name"] == "Chris"


def test_should_restore_name_if_first_name_is_none() -> None:
    user = {
        "first_name": None,
        "last_name": "Clinton",
        "full_name": "Alan Clinton"
    }
    restore_names([user])
    assert user["first_name"] == "Alan"
