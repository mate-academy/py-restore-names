from app.restore_names import restore_names


def test_restore_name_with_none() -> None:
    list_names = [{"full_name": "John Smith", "first_name": None}]
    restore_names(list_names)
    assert list_names == [{"full_name": "John Smith", "first_name": "John"}]


def test_restore_name_without_first_name() -> None:
    list_names = [{"full_name": "John Smith"}]
    restore_names(list_names)
    assert list_names == [{"full_name": "John Smith", "first_name": "John"}]
