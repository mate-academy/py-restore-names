from app.restore_names import restore_names


def test_first_names_is_none() -> None:
    lis = [
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(lis)
    assert lis == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]


def test_without_first_names() -> None:
    lis = [
        {
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
    restore_names(lis)
    assert lis == [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        }
    ]
