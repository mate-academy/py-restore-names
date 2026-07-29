import copy
import app.restore_names as rn


def test_sets_first_name_when_key_missing() -> None:
    users = [
        {"last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    original_id = id(users)

    result = rn.restore_names(users)

    assert result is None  # funkcja nie zwraca nic
    assert id(users) == original_id  # modyfikacja in-place
    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_sets_first_name_when_value_is_none() -> None:
    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"first_name": None, "last_name": "Adams", "full_name": "Mike Adams"},
    ]

    rn.restore_names(users)

    assert users[0]["first_name"] == "Jack"
    assert users[1]["first_name"] == "Mike"


def test_does_not_change_existing_first_name() -> None:
    users = [
        {"first_name": "Anna", "last_name": "Smith",
         "full_name": "Anna Smith"},
        {"first_name": "John", "last_name": "Doe", "full_name": "John Doe"},
    ]
    before = copy.deepcopy(users)

    rn.restore_names(users)

    assert users == before  # jeżeli first_name był, nie powinno się zmienić


def test_uses_first_token_of_full_name() -> None:
    # zabezpieczenie na wypadek, gdy full_name ma więcej niż dwa człony
    users = [
        {
            "first_name": None,
            "last_name": "de la Vega",
            "full_name": "Diego de la Vega",
        }
    ]

    rn.restore_names(users)

    assert users[0]["first_name"] == "Diego"
