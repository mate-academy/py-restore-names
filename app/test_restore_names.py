import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "users, result",
    [
        (
                [
                    {"first_name": None,
                     "last_name": "Holy",
                     "full_name": "Jack Holy"}
                ],
                [
                    {"first_name": "Jack",
                     "last_name": "Holy",
                     "full_name": "Jack Holy"}
                ]
        ),
        (
                [
                    {"last_name": "Heavy",
                     "full_name": "Jack Heavy"}
                ],
                [
                    {"first_name": "Jack",
                     "last_name": "Heavy",
                     "full_name": "Jack Heavy"}
                ]
        ),
        (
                [
                    {"first_name": None,
                     "last_name": "Firstovich",
                     "full_name": "First Firstovich"},
                    {"last_name": "Secondowich",
                     "full_name": "Second Secondowich"}
                ],
                [
                    {"first_name": "First",
                     "last_name": "Firstovich",
                     "full_name": "First Firstovich"},
                    {"first_name": "Second",
                     "last_name": "Secondowich",
                     "full_name": "Second Secondowich"}
                ]
        )
    ]
)
def test_restore_names(users: list[dict],
                       result: list[dict]) -> None:
    assert (
            restore_names(users) == result
    ), (f"Function restore_names should change {users} "
        f"into {result}, but it isn't")
