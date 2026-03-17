import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, expected_first_names",
    [
        ([{"first_name": None, "last_name": "Holy", "full_name": "Jack Holy"}], ["Jack"]),
        ([{"last_name": "Adams", "full_name": "Mike Adams"}], ["Mike"]),
        ([{"first_name": "Anna", "full_name": "Anna Bell"}], ["Anna"]),
        ([{"first_name": None, "full_name": "Cher"}], ["Cher"]),

        ([{"first_name": None, "full_name": ""}], [None]),
        ([{"first_name": None, "full_name": None}], [None]),

        ([{"first_name": None, "full_name": "  John   Doe  "}], ["John"]),

        ([{}], [None]),
        ([{"last_name": "X"}], [None]),

        (
                [
                    {"first_name": None, "full_name": "Alice Wonderland"},
                    {"first_name": "Bob", "full_name": "Bob Builder"}
                ],
                ["Alice", "Bob"]
        ),
    ],
)
def restore_names(users: list[dict]) -> None:
    for user in users:
        if user.get("first_name") is None:
            full_name = user.get("full_name")

            if isinstance(full_name, str) and full_name.strip():
                user["first_name"] = full_name.strip().split()[0]
            else:
                user["first_name"] = None
