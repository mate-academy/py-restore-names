from app.restore_names import restore_names


def test_return_none():
    assert restore_names([{
        "first_name": "Jack",
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }]) is None


def test_without_restore():
    values = [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(values)
    assert values[0]["first_name"] == "Jack"
    assert values[0]["last_name"] == "Holy"
    assert values[0]["full_name"] == "Jack Holy"
    assert values[1]["first_name"] == "Mike"
    assert values[1]["last_name"] == "Adams"
    assert values[1]["full_name"] == "Mike Adams"


def test_with_restore():
    values = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy",
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams",
        },
    ]
    restore_names(values)
    assert values[0]["first_name"] == "Jack"
    assert values[0]["last_name"] == "Holy"
    assert values[0]["full_name"] == "Jack Holy"
    assert values[1]["first_name"] == "Mike"
    assert values[1]["last_name"] == "Adams"
    assert values[1]["full_name"] == "Mike Adams"
