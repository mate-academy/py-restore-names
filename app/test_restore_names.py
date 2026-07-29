from typing import List, Dict, Optional


def test_restore_only_missing_names() -> None:
    def restore_only_missing_names(
        users: List[Dict[str, Optional[str]]]
    ) -> None:
        for user in users:
            if user.get("full_name") and not user.get("first_name"):
                user["first_name"] = user["full_name"].split()[0]

    users = [
        {"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"},
        {"last_name": "Adams", "full_name": "Mike Adams"},
    ]
    restore_only_missing_names(users)

    assert users[0]["first_name"] == "Jack", "First name should be 'Jack'"
    assert users[1]["first_name"] == "Mike", "First name should be 'Mike'"
