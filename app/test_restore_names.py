import pytest
from app.restore_names import restore_names


users = [
    {"first_name": None, "full_name": "Jack Holy"},
    {"full_name": "Mike Adams"},
]

restore_names(users)
assert users[0]["first_name"] == "Jack"
assert users[1]["first_name"] == "Mike"
