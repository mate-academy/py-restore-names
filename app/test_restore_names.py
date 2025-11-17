from app.restore_names import restore_names


def test_restore_only_none_names() -> None:
    # todos os usuários têm first_name = None
    users = [
        {"full_name": "Joana Silva", "first_name": None},
        {"full_name": "Carlos Souza", "first_name": None},
    ]

    restore_names(users)

    assert users == [
        {"full_name": "Joana Silva", "first_name": "Joana"},
        {"full_name": "Carlos Souza", "first_name": "Carlos"},
    ]


def test_restore_only_missing_names() -> None:
    users = [
        {"full_name": "Joana Silva"},
        {"full_name": "Carlos Souza"},
    ]

    restore_names(users)

    assert users == [
        {"full_name": "Joana Silva", "first_name": "Joana"},
        {"full_name": "Carlos Souza", "first_name": "Carlos"},
    ]
