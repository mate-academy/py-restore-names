from app.restore_names import restore_names

users = [
    {
        "full_name": "John Doe",
        "first_name": "John",
    },
    {
        "full_name": "Jane Smith",
        "first_name": None,
    },
    {
        "full_name": "Jim Beam",
        "first_name": None,
    },
    {
        "full_name": "John Doe",
        "first_name": None,
    },
    {
        "full_name": "Jane Smith",
    },
]


def test_restore_names() -> None:
    restore_names(users)

    assert users == [
        {
            "full_name": "John Doe",
            "first_name": "John",
        },
        {
            "full_name": "Jane Smith",
            "first_name": "Jane",
        },
        {
            "full_name": "Jim Beam",
            "first_name": "Jim",
        },
        {
            "full_name": "John Doe",
            "first_name": "John",
        },
        {
            "full_name": "Jane Smith",
            "first_name": "Jane",
        },
    ]
