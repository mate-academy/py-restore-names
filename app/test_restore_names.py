from app.restore_names import restore_names


def test_name_is_none():
    data = [{
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
    }, ]

    restore_names(data)
    assert data[0]["first_name"] == "Jack"


def test_first_name_is_missing():
    data = [{
        "last_name": "Adams",
        "full_name": "Mike Adams",
    }, ]

    restore_names(data)
    assert data[0]["first_name"] == "Mike"
