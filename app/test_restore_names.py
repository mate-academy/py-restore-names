from app.restore_names import restore_names


def test_first_name_none():
    users = [
        dict(first_name=None, last_name="Holy", full_name="Jack Holy")]
    restore_names(users)
    assert users[0]["first_name"] == "Jack"


def test_not_first_name():
    users = [
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        }]
    restore_names(users)
    assert users[0]["first_name"] == "Mike"
