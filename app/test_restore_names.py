import pytest

from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users_input,users_output",
    [
        ([
            {"first_name": None,
             "last_name": "Holy",
             "full_name": "Jack Holy"},
            {"last_name": "Adams",
             "full_name": "Mike Adams"}
        ], [
            {"last_name": "Holy",
             "full_name": "Jack Holy",
             "first_name": "Jack"},
            {"last_name": "Adams",
             "first_name": "Mike",
             "full_name": "Mike Adams"}
        ]),
        ([
            {"last_name": "Adams",
             "full_name": "Mike Adams"}
        ], [
            {"last_name": "Adams",
             "first_name": "Mike",
             "full_name": "Mike Adams"}
        ]),
    ],
    ids=[
        "Users with None first name should be restored correctly.",
        "Users with omitted first name should be restored correctly.",
    ]
)
def test_restored_correctly(users_input: list, users_output: list) -> None:
    restore_names(users_input)
    assert users_input == users_output
