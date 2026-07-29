from app import restore_names


def test_restores_first_name_when_missing_or_none() -> None:
    users = [
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

    result = restore_names.restore_names(users)

    assert result is None
    assert users == [
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


def test_does_not_override_existing_first_name() -> None:
    users = [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
        {
            "first_name": None,
            "last_name": "Brown",
            "full_name": "John Brown",
        },
    ]

    restore_names.restore_names(users)

    assert users == [
        {
            "first_name": "Anna",
            "last_name": "Smith",
            "full_name": "Anna Smith",
        },
        {
            "first_name": "John",
            "last_name": "Brown",
            "full_name": "John Brown",
        },
    ]
