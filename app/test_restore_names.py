import pytest
from app.restore_names import restore_names


@pytest.mark.parametrize(
    "user, expected_user",
    [
        (
            [
                {
                    "first_name": None,
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "last_name": "Adams",
                    "full_name": "Mike Adams",
                },
            ],
            [
                {
                    "first_name": "Jack",
                    "last_name": "Holy",
                    "full_name": "Jack Holy",
                },
                {
                    "first_name": "Mike",
                    "last_name": "Adams",
                    "full_name": "Mike Adams"
                }

            ]
        )
    ]


)
def test_restore_names(user: list[dict],
                       expected_user: list[dict]) -> None:
    restore_names(user)
    assert user == expected_user


@pytest.mark.parametrize(
    "user",
    [
        [{1: 5}],
        [{2: "some"}],
        [{"some": 34}]
    ]
)
def test_type_restore_names(user: list[dict]) -> None:
    with pytest.raises(KeyError):
        restore_names(user)
