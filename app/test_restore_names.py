from app.restore_names import restore_names


def test_without_first_name() -> None:
    data = [{"last_name": "Adams", "full_name": "Mike Adams"}]
    restore_names(data)
    assert data == [
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"}
    ]


def test_with_none_first_name() -> None:
    data = [
        {"first_name": None,
         "last_name": "Adams",
         "full_name": "Mike Adams"}
    ]
    restore_names(data)
    assert data == [
        {"first_name": "Mike",
         "last_name": "Adams",
         "full_name": "Mike Adams"}
    ]
