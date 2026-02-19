import app


def test_restore_names() -> None:
    users = [
        {
            "first_name": None,
            "last_name": "Black",
            "full_name": "Jack Black"
        },
        {
            "first_name": "Emma",
            "last_name": "Holly",
            "full_name": "Emma Holly"
        },
        {
            "last_name": "Smith",
            "full_name": "John Smith"
        },
    ]
    app.restore_names.restore_names(users)

    assert users == [
        {
            "first_name": "Jack",
            "last_name": "Black",
            "full_name": "Jack Black"
        },
        {
            "first_name": "Emma",
            "last_name": "Holly",
            "full_name": "Emma Holly"
        },
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith"
        },
    ]
