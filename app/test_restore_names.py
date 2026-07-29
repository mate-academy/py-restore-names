import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "insert_users,excepted_result",
    [
        pytest.param(
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy"
                }
            ],
            id="should restore name if None"
        ),
        pytest.param(
            [
                {
                    "last_name": "Roronoa",
                    "full_name": "Zoro Roronoa"
                }
            ],
            [
                {
                    "first_name": "Zoro",
                    "last_name": "Roronoa",
                    "full_name": "Zoro Roronoa"
                }
            ],
            id="Should do nothing is dict is full"
        )
    ]
)
def tests(insert_users: list[dict], excepted_result: list[dict]) -> None:
    restore_names(insert_users)
    assert insert_users == excepted_result
