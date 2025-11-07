import pytest
from _pytest.fixtures import FixtureRequest

from app.restore_names import restore_names


UserDict = dict[str, str | None]


@pytest.fixture(params=[
    (0, "pass", 1),
    (1, "pass", 1),
    (1, "dell", 1),
    (1, "mutate", 1),
    (4, "pass", 1),
    (4, "dell", 1),
    (4, "mutate", 1),
    (4, "both", 1),
    (6, "dell", 2),
    (6, "mutate", 2),
    (6, "both", 2),
])
def users_template(request: FixtureRequest) -> list[UserDict]:
    base_user: UserDict = {
        "first_name": "John",
        "full_name": "John Doe",
    }
    users = [base_user.copy() for _ in range(request.param[0])]
    if (action := request.param[1]) == "pass":
        return users

    for i in range(0, request.param[0], request.param[2]):

        if action == "both" and i == 0:
            if "first_name" in users[i]:
                del users[i]["first_name"]
            action = "mutate"
            continue

        if action == "del":
            del users[i]["first_name"]
            continue

        users[i]["first_name"] = None

    return users


def test_restore_names(
        users_template: list[UserDict],
) -> None:
    restore_names(users_template)
    assert all(
        (
            (first_name := user.get("first_name", None))
            and user.get("full_name").split()[0] == first_name
        )
        for user in users_template
    )
