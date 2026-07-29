from app.restore_names import restore_names


users = [
    {
        "first_name": None,
        "last_name": "Holy",
        "full_name": "Jack Holy",
        "expected_name": "Jack",
    },
    {"last_name": "Adams", "full_name": "Mike Adams", "expected_name": "Mike"},
]


def test_restore_names() -> None:
    restore_names(users)
    for user in users:
        assert user["first_name"] == user["expected_name"]
