from app.restore_names import restore_names


def test_restore_names_when_name_none() -> None:
    users = [{"first_name": None,
              "last_name": "Holy",
              "full_name": "Jack Holy"},
             {"first_name": None,
              "last_name": "Shen",
              "full_name": "Vei Shen"}]

    restore_names(users)
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Vei"
    assert isinstance(users[0]["first_name"], str)
    assert restore_names(users) is None


def test_restore_names_when_first_name_valid() -> None:
    users = [{"first_name": "Djo",
              "last_name": "Holy",
              "full_name": "Djo Holy"},

             {"first_name": "Lee",
              "last_name": "Shen",
              "full_name": "Lee Shen"}]

    restore_names(users)
    assert isinstance(users[0]["first_name"], str)
    assert users[0]["first_name"] == "Djo"
    assert users[1]["first_name"] == "Lee"
    assert restore_names(users) is None


def test_restore_names_when_first_name_missing() -> None:
    users = [{"last_name": "Holy",
              "full_name": "Adam Holy"},

             {"last_name": "Shen",
              "full_name": "Volter Shen"}]

    restore_names(users)
    assert all("first_name" in user for user in users)
    assert isinstance(users[0]["first_name"], str)
    assert users[0]["first_name"] == "Adam"
    assert users[1]["first_name"] == "Volter"
    assert restore_names(users) is None
