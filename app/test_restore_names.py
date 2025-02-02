import pytest

def restore_names(users):
    for user in users:
        if not user.get("first_name"):
            user["first_name"] = user["full_name"].split()[0]

@pytest.mark.parametrize("users, expected", [
    ([
        {
            "first_name": None,
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Alice",
            "last_name": "Brown",
            "full_name": "Alice Brown"
        },
        {
            "first_name": None,
            "last_name": "Smith",
            "full_name": "John Smith"
        },
        {
            "last_name": "Smith",
            "full_name": "John Smith"
        }
    ], [
        {
            "first_name": "Jack",
            "last_name": "Holy",
            "full_name": "Jack Holy"
        },
        {
            "first_name": "Mike",
            "last_name": "Adams",
            "full_name": "Mike Adams"
        },
        {
            "first_name": "Alice",
            "last_name": "Brown",
            "full_name": "Alice Brown"
        },
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith"
        },
        {
            "first_name": "John",
            "last_name": "Smith",
            "full_name": "John Smith"
        }
    ])
])
def test_restore_names(users, expected):
    restore_names(users)
    assert users == expected
