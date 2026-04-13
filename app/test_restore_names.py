from app import restore_names


def test_restores_missing_first_name() -> None:
    users = [
        {"full_name": "Ada Lovelace"},
        {"full_name": "Grace Hopper", "first_name": "Grace"},
    ]

    restore_names.restore_names(users)

    assert users == [
        {"full_name": "Ada Lovelace", "first_name": "Ada"},
        {"full_name": "Grace Hopper", "first_name": "Grace"},
    ]


def test_restores_none_first_name() -> None:
    users = [
        {"full_name": "Alan Turing", "first_name": None},
        {"full_name": "Katherine Johnson", "first_name": "Katherine"},
    ]

    restore_names.restore_names(users)

    assert users == [
        {"full_name": "Alan Turing", "first_name": "Alan"},
        {"full_name": "Katherine Johnson", "first_name": "Katherine"},
    ]
